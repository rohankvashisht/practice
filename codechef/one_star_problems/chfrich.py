# Problem Name : Richie Rich

"""
Problem Statement:
Chef aims to be the richest person in Chefland by his new restaurant franchise. Currently, his assets are worth A billion dollars and have no liabilities. He aims to increase his assets by X billion dollars per year.

Also, all the richest people in Chefland are not planning to grow and maintain their current worth.

To be the richest person in Chefland, he needs to be worth at least B billion dollars. How many years will it take Chef to reach his goal if his value increases by X billion dollars each year?

Input:

a. The first line contains an integer TTT, the number of test cases. Then the test cases follow.
b. Each test case contains a single line of input, three integers A, B, X.


Output:
For each test case, output in a single line the answer to the problem.

Constraints:
a. 1 ≤ T ≤ 21000
b. 100 ≤ A < B ≤ 200
c. 1 ≤ X ≤ 50
d. X divides B - A

Sample Input:
3
100 200 10
111 199 11
190 200 10

Sample Output:
10
8
1

Explanation:
Test Case 1: Chef needs to increase his worth by 200 - 100 = 100 billion dollars and his increment per year being 10 billion dollars, so it will take him (100/10) = 10 years to do so.

Test Case 2: Chef needs to increase his worth by 199 - 111 = 88 billion dollars and his increment per year being 11 billion dollars, so it will take him (88/11) = 8 years to do so.

Test Case 3: Chef needs to increase his worth by 200 - 190 = 10 billion dollars and his increment per year being 10 billion dollars, so it will take him (10/10) = 1 years to do so.
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):

  # read integer
  A, B, X = map(int, input().split())
  
  difference_amount = B - A
  
  # round off to nearest whole no. using floor divison
  no_of_years = (difference_amount // X)
  
  print(no_of_years)