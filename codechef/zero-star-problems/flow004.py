# Problem Name : First and Last Digit

"""
Problem Statement:
If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.

Input:
The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N. 

Output:
For each test case, display the sum of first and last digits of N in a new line.

Constraints:
a. 1 ≤ T ≤ 1000
b. 1 ≤ N ≤ 1000000

Sample Input:
3 
1234
124894
242323

Sample Output:
5
5
5
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):
  number = input()
  sum_of_digits = int(number[0]) + int(number[len(number)-1])
  
  print(sum_of_digits)
  