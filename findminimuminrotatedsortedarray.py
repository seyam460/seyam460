from typing import List 

class solution:
    def findMin(self , nums : List[int]) -> int :
        left = 0 
        right = len(nums) -1 
        ans = nums[0]

        while left<= right :
            mid = (right + left) // 2
            ans = min(ans , nums[mid])

            if nums[mid] > nums[right] :
                left = mid + 1
            else :
                right = mid - 1

            return ans
        
sol =  solution()
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([11,13,15,17]))


