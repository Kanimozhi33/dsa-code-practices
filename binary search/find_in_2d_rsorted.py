def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        is_there = False
        for i in range(len(matrix)):
            occurrence = len(matrix[i])
            num_of_ones = 0

            left = 0
            right = len(matrix[i]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    occurrence = mid
                    right = mid - 1

                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if occurrence != len(matrix[i]):
                return True
        return is_there

# the actual soln:



def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    # apply binary search:
    low = 0
    high = n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")


