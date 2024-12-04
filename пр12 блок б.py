def second_largest():
    max_num = float('-inf')
    second_max_num = float('-inf')

    while True:
        num = int(input("Введите натуральное число (0 для завершения): "))
        if num == 0:
            break
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num

    if second_max_num == float('-inf'):
        print("Нет второго по величине элемента.")
    else:
        print(f"Второй по величине элемент: {second_max_num}")

# Запуск функции
second_largest()
