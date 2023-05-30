import sys

def coin_change(coins, amount):
    # Create a table to store the minimum number of coins for each amount
    dp = [sys.maxsize] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != sys.maxsize:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != sys.maxsize else -1

n = int(input("Enter the number of coin denominations: "))
coins = []

print("Enter the coin denominations:")
for _ in range(n):
    coin = int(input())
    coins.append(coin)

amount = int(input("Enter the target amount: "))

min_coins = coin_change(coins, amount)
if min_coins == -1:
    print("Cannot make the exact amount with the given coins.")
else:
    print("Minimum number of coins needed:", min_coins)

    
#The time complexity is O(n * amount), where n is the number of coin denominations and amount is the target amount.
