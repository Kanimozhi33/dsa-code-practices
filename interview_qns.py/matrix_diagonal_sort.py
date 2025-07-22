class Solution:
    def diagonalSort( mat):
        m, n = len(mat), len(mat[0])
        diagonal = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diagonal[i-j].append(mat[i][j])
        for row in diagonal:
            diagonal[row].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonal[i-j].pop()
        return mat



