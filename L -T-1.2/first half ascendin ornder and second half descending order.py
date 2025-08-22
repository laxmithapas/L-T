# Take input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# Sort the array first
arr.sort()

# Find middle point
mid = len(arr) // 2

# First half ascending, second half descending
first_half = arr[:mid]              # already ascending
second_half = arr[mid:][::-1]       # reverse to make descending

# Combine
result = first_half + second_half

print("Result:", result)
