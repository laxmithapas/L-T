n = int(input("Enter a number: "))

n1, n2 = 4, 9
count = 0

print("Fibonacci sequence:")
while count < n:
    print(n1, end = " ")
    nth = n1 + n2
    n1= n2
    n2 = nth
    count += 1