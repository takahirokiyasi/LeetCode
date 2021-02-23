from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (matrix[0][0] > target) or (matrix[-1][-1] < target):
            return False
        else:
            for i in range(len(matrix)):
                if (matrix[i][-1] < target):
                    continue
                else:
                    flag = self.binarySearch(matrix[i], target)
                    if flag:
                        return True
                    else:
                        continue
            return False

    def binarySearch(self, arr, target):
        l = 0
        r = len(arr)-1
        while l <= r:
            m = int((l+r)/2)
            if arr[m] == target:
                return True
            else:
                if arr[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return False
