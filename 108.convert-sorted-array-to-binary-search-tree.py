#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)

        if length == 0:
            return None
        elif length == 1:
            return TreeNode(nums[0])

        mid = length // 2

        left = self.sortedArrayToBST(nums[0:mid])
        right = self.sortedArrayToBST(nums[mid + 1 :])

        return TreeNode(nums[mid], left, right)


# @lc code=end
