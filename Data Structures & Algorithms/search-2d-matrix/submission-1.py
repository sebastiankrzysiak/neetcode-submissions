class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        def is_before(i):
            n = i // C
            m = i % C

            return matrix[n][m] < target
        
        if matrix[0][0] == target:
            return True
        
        l = 0
        r = R * C - 1

        while r - l > 1:
            m = (l + r) // 2
            if is_before(m):
                l = m
            else:
                r = m
        
        n = r // C
        m = r % C

        return matrix[n][m] == target