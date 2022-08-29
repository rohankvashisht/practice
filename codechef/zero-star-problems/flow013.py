# Problem Name : Valid Triangles

"""
Problem Statement:
Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

Input:
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three angles A, B and C, of the triangle separated by space.   

Output:
For each test case, display 'YES' if the triangle is valid, and 'NO', if it is not, in a new line.

Constraints:
a. 1 ≤ T ≤ 1000
b. 1 ≤ A,B,C ≤ 180

Sample Input:
3
40 40 100
45 45 90
180 1 1

Sample Output:
YES
YES
NO
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):
  A, B, C = map(int, input().split())

  if ((A+B+C) == 180) :
    print('YES')
  else :
    print('NO')
  