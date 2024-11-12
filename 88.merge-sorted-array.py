#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy()

        p1 = 0
        p2 = 0

        for i in range(n + m):
            take_1 = p2 >= n or nums1_copy[p1] < nums2[p2]

            if p1 < m and take_1:
                nums1[i] = nums1_copy[p1]
                p1 = p1 + 1
            else:
                nums1[i] = nums2[p2]
                p2 = p2 + 1
   
# @lc code=end

# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]

# Solution().merge(nums1, 3, nums2, 3)

# print(nums1)