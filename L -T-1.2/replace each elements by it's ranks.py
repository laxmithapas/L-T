def replace_with_rank(arr):
    
    sorted_unique = sorted(set(arr))

    
    rank_map = {value: rank+1 for rank, value in enumerate(sorted_unique)}

    
    return [rank_map[x] for x in arr]


arr = [40, 10, 20, 40, 30]
print("Original:", arr)
print("Ranked:", replace_with_rank(arr))
