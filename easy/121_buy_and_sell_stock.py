# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Final Solution
#Minimum price must be set as something super high, so if a number is less than that, it'll save it
#If min price changes, no need to check for profit that day
#Profit only checked if different day from min price
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
            continue

        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        
    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))