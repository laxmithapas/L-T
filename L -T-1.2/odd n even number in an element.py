arr = list(map(int, input("Enter numbers separated by space: ").split()))
odd_numbers = [num for num in arr if num % 2 != 0]
even_numbers = [num for num in arr if num % 2 == 0]
print("Odd numbers are:", odd_numbers)
print("Even numbers are:", even_numbers)
