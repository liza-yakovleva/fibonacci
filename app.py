def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ввод пользователя
n = int(input("Введите значение n: "))

print(f"Число Фібоначчі для n = {n}: {fibonacci(n)}")
