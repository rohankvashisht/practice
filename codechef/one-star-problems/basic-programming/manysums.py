# Problem Name : Distinct Pair Sums

"""
Problem Statement:
You are given a range of integers {L,L+1,…,R}. An integer X is said to be reachable if it can be represented as a sum of two not necessarily distinct integers in this range. Find the number of distinct reachable integers.

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains two space-separated integers L and R.


Output Format:
For each test case, print a single line containing one integer — the number of reachable integers.

Constraints:
a. 1 ≤ T ≤ 10^5
b. 1 ≤ L < R ≤ 10^6

Sample Input 1:
2
2 2
2 3

Sample Output 1:
1
3

Explanation:
Example Case 1: The only reachable integer is 2+2=4.

Example Case 2: 4, 5 and 6 are reachable, since 2 + 2 = 4, 2 + 3 = 5 and 3 + 3 = 6.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read integers
  L, R = map(int, input().split())
  
  # calculate range
  N = R - L
  
  # Distinct reachable integers L+L to R+R
  print(2*N + 1)
  