class Solution():
    def maxProfit(self, prices:list)->int:
        
        price_min = 10000 # 최저 주식값
        profit = 0 # 수익
        
        for price_current in prices:
            price_min = min(price_current, price_min)
            profit = max(profit, price_current-price_min) 
        return profit