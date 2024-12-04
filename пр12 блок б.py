def find_numbers(numbers):
    if len(numbers) == 0:
        return None, None
    
    first = numbers[0]
    rest_first, rest_second = find_numbers(numbers[1:])
    
    if rest_first is None:  # первый элемент - единственный в последовательности
        return first, None
    
    if first > rest_first:
        return first, max(rest_first, second if rest_second is None else rest_second)
    else:
        return rest_first, max(first, second if rest_second is None else rest_second)

def get_numbers():
    num = int(input("Введите натуральное число (0 для завершения): "))
    if num == 0:
        return []
    else:
        return [num] + get_numbers()

numbers = get_numbers()
first, second = find_numbers(numbers)

if second is not None:
    print(f"Второй по величине элемент: {second}")
else:
    print("Второго по величине элемента нет.")
