# Problem Name : Add Two Numbers

"""
Problem Statement:
Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.

The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

Input:
The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.

Output:
For each test case, add A and B and display the sum in a new line.

Constraints:
N.A.

Sample Input:
3
1 2
100 200
10 40

Sample Output:
3
300
50
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):
	# read integers a and b.
	(a, b) = map(int, input().split(' '))
	result = a + b

	# print result in required format
	print(result)
