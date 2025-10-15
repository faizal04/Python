def coin_change(coins, amount):
    # Initialize DP table with a value larger than any possible answer
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
                
    return dp[amount] if dp[amount] != float('inf') else -1

# Test
print(f"Min Coins: {coin_change([1, 2, 5], 11)}") 
# Output: 3 (5 + 5 + 1)