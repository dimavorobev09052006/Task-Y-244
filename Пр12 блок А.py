def power(x, n):
    """Рекурсивно вычисляет x^n."""
    if n == 0:
        return 1
    return x * power(x, n - 1)

def factorial(n):
    """Рекурсивно вычисляет n!"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_expression(x, n):
    """Вычисляет x^n / n!"""
    return power(x, n) / factorial(n)

# Пример использования
x = int(input("Введите натуральное число x: "))
n = int(input("Введите натуральное число n: "))

# Проверка на натуральные числа
if x < 1 or n < 1:
    print("Оба числа должны быть натуральными.")
else:
    result = calculate_expression(x, n)
    print(f"Результат: {result}")
