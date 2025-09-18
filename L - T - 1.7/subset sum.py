def subset_sum_backtrack(arr, target):
    result = []

    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path, current_sum + arr[i])
            path.pop()

    backtrack(0, [], 0)
    return result

# Example usage
arr = [3, 34, 4, 12, 5, 2]
target = 9
solutions = subset_sum_backtrack(arr, target)
for sol in solutions:
    print(sol)

