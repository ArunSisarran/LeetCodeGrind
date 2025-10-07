'''
idea:
since each row is sorted in increasing order and the beginning of each row is always greater
than the last element in the last row, we check the last row element to see if the target 
would be in range of that row. Then we preform binary search on that row
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = 0

        # while we are in bounds of the matrix
        while row < rows:

            # check if the target is within the range of the current row
            if matrix[row][col] <= target <= matrix[row][cols - 1]:
                l = 0
                r = cols - 1

                while l <= r:
                    m = l + (r - l) // 2

                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                    
                # if it passed the binary search and didnt return true it means the 
                # element does not exist in the matrix so return false
                return False
            else:
                row += 1

        return False


        