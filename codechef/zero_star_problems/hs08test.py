# Problem Name : ATM

"""
Problem Statement:
Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.

Calculate Pooja's account balance after an attempted transaction

Input:
Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance. 

Output:
Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

Constraints:
a. 0 ≤ n ≤ 105

Sample Input:
30 120.00

Sample Output (Successful Transaction):
89.50

Sample Input:
42 120.00

Sample Output (Incorrect Withdrawal Amount (not multiple of 5)):
120.00

Sample Input:
300 120.00

Sample Output (Insufficient Funds):
120.00
"""

# cook your dish here

withdraw_amt, total_amt = map(float, input().split())
withdraw_amt = int(withdraw_amt)

bank_charges = 0.5
remaining_amt = total_amt-(withdraw_amt+bank_charges)

# code logic
if ((withdraw_amt+bank_charges)<=total_amt and (withdraw_amt%5==0)):
    print(float(remaining_amt))
else:
    print(float(total_amt))