# Problem Name : Sum of Digits

"""
Problem Statement:
You're given an integer N. Write a program to calculate the sum of all the digits of N. 

Input:
The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N. 

Output:
For each test case, calculate the sum of digits of N, and display it in a new line.

Constraints:
a. 1 ≤ T ≤ 1000
b. 1 ≤ A, B ≤ 1000000

Sample Input:
3 
12345
31203
2123

Sample Output:
15
9
8
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):
  number = int(input())
  sum_of_digits = 0
  for i in str(number):
    sum_of_digits += int(i)
  
  print(sum_of_digits)
  