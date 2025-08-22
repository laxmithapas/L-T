n = int(input("Enter the size of the matrix (n x n):"))

def spiral_traversal(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    result = []

    while left <= right and top <= bottom:
        # 1. Traverse left → right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # 2. Traverse top → bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # 3. Traverse right → left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # 4. Traverse bottom → top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result