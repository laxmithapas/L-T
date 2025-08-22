n = list(map(int, input("Enter numbers separated by space: ").split()))
ranks = {val: rank for rank, val in enumerate(sorted(set(n)), start=1)}
replaced = [ranks[val] for val in n]
print("Replaced array is:", replaced)
