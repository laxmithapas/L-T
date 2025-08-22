
arr = list(map(int, input("Enter numbers separated by space: ").split()))


max_value = arr[0]
for num in arr:
    if num > max_value:
        max_value = num

second_max = float('-inf')
for num in arr:
    if num != max_value and num > second_max:
        second_max = num

if second_max == float('-inf'):
    print("No second largest element.")
else:
    print("Second largest element is:", second_max)
