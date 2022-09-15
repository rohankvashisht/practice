# Problem Name : Chef And Operators

"""
Problem Statement:
Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.
Relational Operators are operators which check relatioship between two values. Given two numerical values A and B you need to help chef in finding the relationship between them that is,
First one is greater than second or, First one is less than second or, First and second one are equal.

Input:
First line contains an integer T, which denotes the number of testcases. Each of the T lines contain two integers A and B.    

Output:
For each line of input produce one line of output. This line contains any one of the relational operators '<' , '>' , '='.

Constraints:
a. 1 ≤ T ≤ 10000
b. 1 ≤ A,B ≤ 1000000001

Sample Input:
3
10 20
20 10
10 10

Sample Output:
<
>
=
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  A, B = map(int, input().split())

  if A < B :
    print('<')
  elif A > B :
    print('>')
  else :
    print('=')
  