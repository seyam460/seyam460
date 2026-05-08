from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for number in nums[1:]:
            current_sum = max(number, current_sum + number)
            max_sum = max(max_sum, current_sum)

        return max_sum
    

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) 

