from typing import List 

class solution :
    def maxprofit(self , prices: List[int]) -> int :
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit
    
sol = solution()
result = sol.maxprofit([7,1,5,3,6,4])
print("output: ", result)




