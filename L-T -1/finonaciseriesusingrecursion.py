def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("Enter the position in Fibonacci sequence: "))
print("Fibonacci number at position", num, "is", fibonacci(num))
