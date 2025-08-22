# Bubble Sort
arr = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]  # swap

print("Sorted array:", arr)
