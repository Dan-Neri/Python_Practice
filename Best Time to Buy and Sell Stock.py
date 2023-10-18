"""
You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot 
achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 
6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must 
buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 

Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104
"""

class Solution:
    #Strategy: If we iterate through prices and keep track of the lowest price
        #price and the highest price, we will be done except in one case: If 
        #the lowest price comes after the highest price. If we keep track of
        #of two possible buy dates we can keep whichever one produces the
        #highest profit and forget the other.

    #Time complextiy: O(N)
    #Space complexity: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        buy, newBuy, sell, profit = 0, 0, 0, 0
        for i in range(1, len(prices)):
            #If the price is lower than our current buy price, it's a possible
            #better buy date
            if prices[i] < prices[newBuy]:
                newBuy = i
            #If the price is higher than our current sell price, replace it and
            #recalculate profit
            elif prices[i] >= prices[sell]:
                sell = i
                profit = prices[sell] - prices[buy]
            #If the new buy date produces a better profit, replace the buy date
            #and the sell date and update profit.
            if prices[i]-prices[newBuy] > profit:
                sell = i
                buy = newBuy
                profit = prices[sell] - prices[buy]
        return profit