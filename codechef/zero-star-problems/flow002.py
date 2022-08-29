# Problem Name : Find Remainder

"""
Problem Statement:
Write a program to find the remainder when an integer A is divided by an integer B.

Input:
The first line contains an integer T, the total number of test cases. Then T lines follow, each line contains two Integers A and B.

Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance. 

Output:
For each test case, find the remainder when A is divided by B, and display it in a new line.

Constraints:
a. 1 ≤ T ≤ 1000
b. 1 ≤ A, B ≤ 10000

Sample Input:
3 
1 2
100 200
40 15

Sample Output (Successful Transaction):
1
100
10
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):
  A, B = map(int, input().split())
  print(A%B)