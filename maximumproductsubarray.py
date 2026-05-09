from typing import List 

class solution :
    def maxproduct(self , nums : List[int]) -> int :
        cur_min = nums[0]
        cur_max = nums[0]
        global_max = nums[0]

        for num in nums[1: ] :
            if num<0 :
                cur_min , cur_max = cur_max , cur_min
            
            cur_min = min(num , cur_min*num)
            cur_max = max(num , cur_max*num)
            global_max = max(global_max , cur_max)

            return global_max
        
sol = solution()
print(sol.maxproduct([2,3,-2,4]))
print(sol.maxproduct([-2,0,-1]))
print(sol.maxproduct([-2,3,-4]))
