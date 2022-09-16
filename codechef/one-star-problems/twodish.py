# Problem Name : Two Dishes

"""
Problem Statement:
Chef will have N guests in his house today. He wants to serve at least one dish to each of the N guests. Chef can make two types of dishes. He needs one fruit and one vegetable to make the first type of dish and one vegetable and one fish to make the second type of dish. Now Chef has A fruits, B vegetables, and C fishes in his house. Can he prepare at least N dishes in total?

Input Format:
a. First line will contain T, number of test cases. Then the test cases follow.
b. Each test case contains of a single line of input, four integers N, A, B, C.


Output Format:
For each test case, print "YES" if Chef can prepare at least N dishes, otherwise print "NO". Print the output without quotes.

Constraints:
a. 1 ≤ T ≤ 100
b. 1 ≤ N, A, B, C ≤ 100

Sample Input 1:
4
2 1 2 1
3 2 2 2
4 2 6 3
3 1 3 1

Sample Output 1:
YES
NO
YES
NO

Explanation:
Test Case 1: Chef prepares one dish of the first type using one fruit and one vegetable and another dish of the second type using one vegetable and one fish.

Test Case 2: Chef prepares two dishes of the first type using two fruit and two vegetable. Now all the vegetables are exhausted, hence he can't prepare any other dishes.

Test Case 3: Chef can prepare a total of 5 dishes, two dishes of the first type and three dishes of the second type.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):

  # read number of guests, fruits, vegetables and fishes
  N, A, B, C = map(int, input().split())
  
  # find which is limiting B or (A+C) ?
  if B > A+C :
    if N <= (A+C) :
      print('YES')
    else:
      print ('NO') 
  elif B < A+C :
    if N <= B :
      print('YES')
    else:
      print ('NO')
  else :
    if N <= B :
      print('YES')
    else:
      print ('NO')