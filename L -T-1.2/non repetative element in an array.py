arr = list(map(int, input("Enter numbers separated by space: ").split()))
non_repetitive = []
for num in arr:
    if arr.count(num) == 1:
        non_repetitive.append(num)
print("Non-repetitive elements are:", non_repetitive)
