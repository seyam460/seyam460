from typing import List 

class Solution : 
    def containsDuplicate(self , nums:List[int]) -> bool :
        seen = set()

        for num in nums :
            if num in seen :
                return True 
            seen.add(num)

        return False
    
sol = Solution()
print("output: " , sol.containsDuplicate([1,2,3,4,9,6,7,8,9,10])) 
print("output: " , sol.containsDuplicate([1,2,3,4,5,6,7,3,9,10]))
print("output: " , sol.containsDuplicate([1,2,3,4,5,6,7,8,9,10]))




