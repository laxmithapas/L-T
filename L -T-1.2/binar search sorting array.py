# Binary Search
key = int(input("Enter the number to search: "))

low, high = 0, len(arr)-1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at index:", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
