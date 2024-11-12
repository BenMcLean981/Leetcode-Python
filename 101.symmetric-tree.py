#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return isSameTree(root.left, reverse(root.right))


def reverse(node: Optional[TreeNode]) -> Optional[TreeNode]:
    if node is None:
        return None

    return TreeNode(node.val, reverse(node.right), reverse(node.left))


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None and q is not None:
        return False
    elif p is not None and q is None:
        return False
    else:
        return (
            p.val == q.val
            and isSameTree(p.left, q.left)
            and isSameTree(p.right, q.right)
        )


# @lc code=end
