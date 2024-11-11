#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
import math
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = from_digits(digits)

        return to_digits(num + 1)
        
def from_digits(digits: List[int]) -> int:
    return sum(d * 10 ** i for i, d in enumerate(digits[::-1]))

def to_digits(n: int) -> List[int]:
    return [get_digit(n, i) for i in range(get_num_digits(n))][::-1]

def get_num_digits(n: int) -> int:
    return math.floor(math.log10(n)) + 1

def get_digit(n: int, place: int) -> int:
    return n // (10 ** place) % 10

# @lc code=end

