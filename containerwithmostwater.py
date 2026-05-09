from typing import List 

class solution :
    def maxarea (self ,  height : List[int]) -> int :
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right :
            width = right - left 
            h = min (height[left] , height[right])
            max_area = max ( max_area , width * h)

            if height[left] < height[right] :
                left += 1
            else :
                right -= 1 
        return max_area
    
sol = solution()
print(sol.maxarea([1,8,6,2,5,4,8,3,7]))
print(sol.maxarea([1,1,7,5,3]))

