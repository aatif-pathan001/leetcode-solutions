"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Time Complexity: O(n)
Space Complexity: O(1)

Approach: Track minimum price seen so far and maximum profit
Key insight: Profit = sell_price - buy_price
We want to buy at lowest price before we sell

What I learned:
Keep track of running minimum/maximum
One pass through array is enough
O(1) space by using variables instead of arrays

Mistakes:
Don't try all pairs (O(n²)) - too slow


"""



def maxProfit1(prices):
        buy = prices[0]
        sell = prices[0]
        max_profit = 0

        for price in prices:
            if price < buy:
                buy = price
                sell = buy
            if price > sell:
                sell = price
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit

        return max_profit


def maxProfit2(prices):
  if not prices:
    return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)

        # Calculate profit if we sell at current price
        profit = price - min_price

        # Update maximum profit
        max_profit = max(max_profit, profit)

    return max_profit
