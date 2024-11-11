#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        if x == 0:
            return 0
        elif x <= 3:
            return 1

        while True:
            n = (low + high) // 2
            
            n_low = n - 1
            n_squared = n * n
            n_low_squared = n_low * n_low
            
            if n_squared == x:
                return n
            elif n_low_squared < x < n_squared:
                return n_low
            elif n_squared > x:
                high = n
            else:
                low = n
                    
# @lc code=end
