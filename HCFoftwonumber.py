def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)
 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("HCF is", hcf(num1, num2))
