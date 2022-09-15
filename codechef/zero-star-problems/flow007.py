# Problem Name : Reverse The Number

"""
Problem Statement:
Given an Integer N, write a program to reverse it.

Input:
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.  

Output:
For each test case, display the reverse of the given number N, in a new line.

Constraints:
a. 1 ≤ T ≤ 1000
b. 1 ≤ N ≤ 1000000

Sample Input:
4
12345
31203
2123
2300

Sample Output:
54321
30213
3212
32
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  number = int(input())

  reverse_number = 0
  
  while(number):
        remainder = number%10
        reverse_number =reverse_number*10+remainder
        number = int(number/10)

  print(reverse_number)
  