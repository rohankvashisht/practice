# Problem Name : Playing with Matches

"""
Problem Statement:
Chef's son Chefu found some matches in the kitchen and he immediately starting playing with them.

The first thing Chefu wanted to do was to calculate the result of his homework — the sum of A and B, and write it using matches. Help Chefu and tell him the number of matches needed to write the result.

Digits are formed using matches in the following way:
a. Zero - requires 6 matches
b. One - requires 2 matches
c. Two - requires 5 matches
d. Three - requires 5 matches
e. Four - requires 4 matches
f. Five - requires 5 matches
g. Six - requires 6 matches
h. Seven - requires 3 matches
i. Eight - requires 7 matches
j. Nine - requires 6 matches

Input:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains two space-separated integers A and B.

Output:
For each test case, print a single line containing one integer — the number of matches needed to write the result (A+B).

Constraints:
a. 1 ≤ T ≤ 1000
b. 1 ≤ A,B ≤ 10^6


Sample Input:
3
123 234
10101 1010
4 4

Sample Output:
13
10
7

Explanation: 
Example case 1: The result is 357. We need 5 matches to write the digit 3, 5 matches to write the digit 5 and 3 matches to write the digit 7.

Example case 2: The result is 11111. We need 2 matches to write each digit 1, which is 2⋅5=10 matches in total.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):

  # read number of guests, fruits, vegetables and fishes
  A, B = map(int, input().split())
  
  sum = str(A + B)
  no_of_matches = 0
  
  for digit in sum:
    if (digit == '0') or (digit == '6') or (digit == '9'):
      no_of_matches += 6
    elif (digit == '2') or (digit == '3') or (digit == '5'):
      no_of_matches += 5
    elif (digit == '1'):
      no_of_matches += 2
    elif (digit == '4'):
      no_of_matches += 4
    elif (digit == '7'):
      no_of_matches += 3
    else:
      no_of_matches += 7
    
  print(no_of_matches)