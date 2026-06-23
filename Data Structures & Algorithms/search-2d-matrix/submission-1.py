class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row = 0

        while top <= bottom:
            mid = (top+bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif target <= matrix[mid][-1] and target >= matrix[mid][0]:
                row = mid
                break

        
        low = 0
        high = len(matrix[0]) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                low = mid + 1
            elif target < matrix[row][mid]:
                high = mid - 1
        

        return False
