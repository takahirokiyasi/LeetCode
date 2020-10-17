class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        combined.sort()
        if len(combined) % 2 == 0:
            return (combined[int(len(combined) / 2) - 1] + combined[int(len(combined) / 2)]) / 2
        return combined[int(len(combined) / 2)]
