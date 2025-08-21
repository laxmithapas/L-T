def summation(a, b):
    if b == 0:
        return a
    return summation(a + 1, b - 1)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Summation is:", summation(num1, num2))