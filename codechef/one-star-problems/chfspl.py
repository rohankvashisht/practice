# Problem Name : Vaccine Dates

"""
Problem Statement:
Chef has three spells. Their powers are A, B, and C respectively. Initially, Chef has 000 hit points, and if he uses a spell with power P, then his number of hit points increases by P.

Before going to sleep, Chef wants to use exactly two spells out of these three. Find the maximum number of hit points Chef can have after using the spells.

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains three space-separated integers A, B, and C.


Output Format:
For each test case, print a single line containing one integer — the maximum number of hit points.

Constraints:
a. 1 ≤ T ≤ 10^4
b. 1 ≤ A, B, C ≤ 10^8

Sample Input 1:
2
4 2 8
10 14 18

Sample Output 1:
12
32

Explanation:
Example Case 1: Chef has three possible options:
a. Use the first and second spell and have 4 + 2 = 6 points.
b. Use the second and third spell and have 2 + 8 = 10 points.
c. Use the first and third spell and have 4 + 8 = 12 points.

Chef should choose the third option and use the spells with power 4 and 8 to have 12 hitpoints.

Example Case 2: Chef should use the spells with power 14 and 18.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):

  # read three powers
  A, B, C = map(int, input().split())
  
  # print maximum of three possible combinations
  print (max(A+B, B+C, C+A))