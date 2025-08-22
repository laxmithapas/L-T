arr = list(map(int, input("Enter numbers separated by space: ").split()))
num = int(input("Enter the number to find its frequency: "))
frequency = arr.count(num)
print("Frequency of", num, "is:", frequency)
