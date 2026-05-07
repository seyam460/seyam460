from typing import List 

class solution:
    def twosum(self, nums:list[int], target: int) -> List[int]:
        seen = dict()

        for  i , num in enumerate (nums):
            needed =  target - num 

            if needed in seen :
                return (seen[needed] , i)

            seen[num] = i

        return []
    

sol = solution()
result = sol.twosum([2,4,6,2],4)
print("output: ", result)

