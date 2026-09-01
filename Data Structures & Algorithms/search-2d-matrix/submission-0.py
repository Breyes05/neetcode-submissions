class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2D matrix
        low_i = 0
        low_j = 0
        high_i = len(matrix) - 1
        high_j = len(matrix[0]) - 1
        # pin point the specific array first
        while (low_i <= high_i):
            middle_i = low_i + (high_i - low_i) // 2
            if (matrix[middle_i][0] <= target and matrix[middle_i][high_j] >= target):
                break
            if (matrix[middle_i][0] < target):
                low_i = middle_i + 1
            elif (matrix[middle_i][high_j] > target):
                high_i = middle_i - 1
        # pinpoint nested array that possibly contains value
        
        while (low_j <= high_j):
            middle_j = low_j + (high_j - low_j) // 2
            if (matrix[middle_i][middle_j] == target):
                return True
            elif (matrix[middle_i][middle_j] < target):
                low_j = middle_j + 1
            elif (matrix[middle_i][middle_j] > target):
                high_j = middle_j - 1
        # pinpoint value
        return False