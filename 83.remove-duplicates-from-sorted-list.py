#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        seen = { head.val }

        result_head = ListNode(head.val)
        current_result = result_head

        current = head.next

        while current is not None:
            if current.val not in seen:
                seen.add(current.val)
                current_result.next = ListNode(current.val)
                current_result = current_result.next

            current = current.next

        return result_head


# @lc code=end