from typing import List


def coin_changes(coins: List[int], amount: int) -> int:
    """Calculate minimum number of coins needed"""
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for i in range(amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return -1 if dp[amount] > amount else dp[amount]


def main():
    coins = [1, 2, 5]
    amount = 16
    print(coin_changes(coins, amount))


if __name__ == "__main__":
    main()
