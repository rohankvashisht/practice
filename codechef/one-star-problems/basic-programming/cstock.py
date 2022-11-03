# Problem Name : Chef and Stock Prices

"""
Problem Statement:
Chef wants to buy a stock whose price was S rupees when the market opened. He will buy the stock if and only if its price is in the range [A,B]. The price of the stock has changed by C% by the time he was trying to buy the stock. Will he be able to buy the stock?

Input Format:
a. First line of the input contains T, the number of testcases. Then the test cases follow.
b. Each test case contains 444 space-separated integers S,A,B,C in a single line.


Output Format:
For each test case, if Chef buys the stock print YES, otherwise print NO.

You may print each character of the string in uppercase or lowercase (for example, the strings yEs, yes, Yes, and YES will all be treated as identical).

Constraints:
a. 1 ≤ T ≤ 1000
b. 0 ≤ S ≤ 10^6
c. 0 ≤ A ≤ B ≤ 10^6
d. -100 ≤ C ≤ 100

Sample Input 1:
3
100 93 108 7
100 94 100 -7
183 152 172 -17

Sample Output 1:
Yes
No
No

Explanation:
Test Case 1: The price of the stock after gaining 7% will become 107, which is in Chef's range of [93,108]. Hence, Chef will buy the stock.

Test Case 2: The price of the stock after falling 7% will become 93, which is not in Chef's range of [94,100]. Hence, Chef will not buy the stock.

Test Case 3: The price of the stock after falling 17% will become 151.89, which is not in Chef's range of [152,172]. Hence, Chef will not buy the stock.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read integers
  S, A, B, C = map(int, input().split())
  
  # update stock price based on recent change
  S = S*(1+(C/100))
  
  # test for purchase condition
  if A <= S <=B :
    print('Yes')
  else :
    print('No')