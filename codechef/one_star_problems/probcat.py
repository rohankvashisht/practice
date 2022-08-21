# Problem Name : Problem Category

"""
Problem Statement:
Chef prepared a problem. The admin has rated this problem for xxx points.

A problem is called:

a. Easy if 1 ≤ x < 100

b. Medium if 100 ≤ x < 200

c. Hard if 200 ≤ x ≤ 300

Find the category to which Chef's problem belongs.

Input:

a. The first line contains TTT denoting the number of test cases. Then the test cases follow.
b. The first and only line of each test case contains a single integer xxx.


Output:
For each test case, output in a single line the category of Chef's problem, i.e whether it is an Easy, Medium or Hard problem. The output is case sensitive.

Constraints:
1 ≤ T ≤ 50
1 ≤ x ≤ 300

Sample Input:
3
50
172
201

Sample Output:
Easy
Medium
Hard
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):

  # read integer
  X = int(input())

  if 1 <= X < 100:
    print('Easy')
  elif 100 <= X < 200:
    print('Medium')
  elif 200 <= X <= 300:
    print('Hard')
  else:
    print('Input value out of bounds')