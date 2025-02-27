class Solution:
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



def searchElement(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1

    # Traverse the matrix from (0, m-1):
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 8)
print("true" if result else "false")


