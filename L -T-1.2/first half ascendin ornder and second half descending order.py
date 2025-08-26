
arr = list(map(int, input("Enter numbers separated by space: ").split()))


arr.sort()


mid = len(arr) // 2


first_half = arr[:mid]              
second_half = arr[mid:][::-1]       


result = first_half + second_half

print("Result:", result)
