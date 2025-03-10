class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m is equal to how many rows there are in the matrix 
        m = len(matrix)
        # n is equal to the number of columns their are in the matrix 
        n = len(matrix[0])
        # t is the total number of entries in the matrix
        t = m * n
        # l and r are just the two pointers
        l = 0
        r = t - 1

        while l <= r:

            # M is the middle formula
            M = (l+r)//2
            # i is the row index
            i = M // n
            # j is the column index
            j = M % n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = M + 1
            else:
                r = M - 1

        return False
