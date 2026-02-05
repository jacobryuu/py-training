from decimal import Decimal, ROUND_UP
from typing import Dict, List
from collections import OrderedDict


class MinimumCoinChangeCalculator:
    UNIT_PRICE = Decimal('1.2')
    
    @staticmethod
    def print_change(change_breakdown: Dict[int, int], title: str = "Change Result:"):
        """Prints the change breakdown"""
        print(title)
        if not change_breakdown:
            print("  No change could be calculated or is needed.")
            return
        print("  Change breakdown:")
        for bill, count in change_breakdown.items():
            print(f"  Bill: {bill}, Count: {count}")
    
    @staticmethod
    def calculate_change(cash_register: Dict[int, int], payment_amount: int, quantity: int) -> Dict[int, int]:
        """
        Calculates change using greedy algorithm
        
        Args:
            cash_register: Available bills/coins and their counts
            payment_amount: Amount paid by customer
            quantity: Number of items purchased
            
        Returns:
            Dictionary of bill value to count, or empty dict if change cannot be made
        """
        # Calculate total price
        total_price = int((MinimumCoinChangeCalculator.UNIT_PRICE * quantity).quantize(Decimal('1'), rounding=ROUND_UP))
        
        if payment_amount < total_price:
            print(f"Payment amount ({payment_amount}) is less than total price ({total_price}).")
            return {}
        
        if payment_amount == total_price:
            print("Payment is exact. No change needed.")
            return {}
        
        change_amount = payment_amount - total_price
        print(f"Total price: {total_price}, Payment: {payment_amount}, Change to be given: {change_amount}")
        
        available_cash_amount = sum(bill * count for bill, count in cash_register.items())
        
        if available_cash_amount < change_amount:
            print(f"Not enough total cash in the register ({available_cash_amount}) to make change for {change_amount}.")
            return {}
        
        # Greedy approach: start from largest denomination
        bill_values = sorted(cash_register.keys(), reverse=True)
        change_breakdown = OrderedDict()
        
        for bill_value in bill_values:
            if change_amount == 0:
                break
            
            available_bills = cash_register.get(bill_value, 0)
            if available_bills == 0:
                continue
            
            bills_to_use = min(change_amount // bill_value, available_bills)
            
            if bills_to_use > 0:
                change_breakdown[bill_value] = bills_to_use
                change_amount -= bill_value * bills_to_use
        
        if change_amount != 0:
            print(f"Could not make exact change. Remaining amount: {change_amount}")
            return {}
        
        return change_breakdown
    
    @staticmethod
    def calculate_change_dp(cash_register: Dict[int, int], payment_amount: int, quantity: int) -> Dict[int, int]:
        """
        Calculates optimal change using dynamic programming
        
        Args:
            cash_register: Available bills/coins and their counts
            payment_amount: Amount paid by customer
            quantity: Number of items purchased
            
        Returns:
            Dictionary of bill value to count, or empty dict if change cannot be made
        """
        total_price = int((MinimumCoinChangeCalculator.UNIT_PRICE * quantity).quantize(Decimal('1'), rounding=ROUND_UP))
        
        if payment_amount < total_price:
            print(f"[DP] Payment amount ({payment_amount}) is less than total price ({total_price}).")
            return {}
        
        if payment_amount == total_price:
            print("[DP] Payment is exact. No change needed.")
            return {}
        
        change_amount = payment_amount - total_price
        print(f"[DP] Total price: {total_price}, Payment: {payment_amount}, Change to be given: {change_amount}")
        
        available_cash_amount = sum(bill * count for bill, count in cash_register.items())
        if available_cash_amount < change_amount:
            print(f"[DP] Not enough total cash in the register ({available_cash_amount}) to make change for {change_amount}.")
            return {}
        
        # DP Implementation for Bounded Coin Change
        dp = [change_amount + 1] * (change_amount + 1)
        last_coin = [0] * (change_amount + 1)
        dp[0] = 0
        
        # Create list of all individual coins
        all_coins = []
        for bill_value, count in cash_register.items():
            all_coins.extend([bill_value] * count)
        
        # DP calculation
        for coin in all_coins:
            for j in range(change_amount, coin - 1, -1):
                if dp[j - coin] + 1 < dp[j]:
                    dp[j] = dp[j - coin] + 1
                    last_coin[j] = coin
        
        if dp[change_amount] > change_amount:
            print("[DP] Could not make exact change with the available denominations.")
            return {}
        
        # Reconstruct the change breakdown
        change_breakdown = {}
        current_amount = change_amount
        while current_amount > 0:
            coin_used = last_coin[current_amount]
            change_breakdown[coin_used] = change_breakdown.get(coin_used, 0) + 1
            current_amount -= coin_used
        
        return change_breakdown


def main():
    # Initialize cash register
    cash_register = {
        10000: 3,
        5000: 3,
        1000: 3,
        500: 5,
        100: 5,
        50: 5,
        10: 5,
        1: 100
    }
    
    # Example 1: Successful change calculation
    print("--- Example 1: payment 10000, quantity 30 ---")
    change_breakdown1 = MinimumCoinChangeCalculator.calculate_change(cash_register, 10000, 30)
    MinimumCoinChangeCalculator.print_change(change_breakdown1, "Greedy Result")
    
    # Example 2: Not enough payment
    print("\n--- Example 2: payment 30, quantity 30 (Not enough payment) ---")
    change_breakdown2 = MinimumCoinChangeCalculator.calculate_change(cash_register, 30, 30)
    MinimumCoinChangeCalculator.print_change(change_breakdown2, "Greedy Result")
    
    # Example 3: Not enough cash in register
    print("\n--- Example 3: payment 100000, quantity 1 (Not enough cash in register) ---")
    change_breakdown3 = MinimumCoinChangeCalculator.calculate_change(cash_register, 100000, 1)
    MinimumCoinChangeCalculator.print_change(change_breakdown3, "Greedy Result")
    
    # Example 4: Exact change not possible
    difficult_cash_register = {10: 5, 5: 5}
    print("\n--- Example 4: payment 9, quantity 1 (price 2 -> change 7), with only 5s and 10s ---")
    change_breakdown4 = MinimumCoinChangeCalculator.calculate_change(difficult_cash_register, 9, 1)
    MinimumCoinChangeCalculator.print_change(change_breakdown4, "Greedy Result")
    
    # Example 5: Greedy vs DP
    print("\n--- Example 5: Greedy vs DP (non-canonical coin system) ---")
    non_canonical_register = {6: 5, 4: 5, 1: 10}
    print("Goal: Make change for 8 with coins {1, 4, 6}")
    greedy_result = MinimumCoinChangeCalculator.calculate_change(non_canonical_register, 10, 1)
    MinimumCoinChangeCalculator.print_change(greedy_result, "Greedy Result (Sub-optimal)")
    
    dp_result = MinimumCoinChangeCalculator.calculate_change_dp(non_canonical_register, 10, 1)
    MinimumCoinChangeCalculator.print_change(dp_result, "DP Result (Optimal)")


if __name__ == "__main__":
    main()
