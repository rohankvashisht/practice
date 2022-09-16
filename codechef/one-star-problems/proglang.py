# Problem Name : Programming Languages

"""
Problem Statement:
Chef is a software developer, so he has to switch between different languages sometimes. Each programming language has some features, which are represented by integers here.

Currently, Chef has to use a language with two given features A and B. He has two options --- switching to a language with two features A1 and B1, or to a language with two features A2 and B2. All four features of these two languages are pairwise distinct.

Tell Chef whether he can use the first language, the second language or neither of these languages (if no single language has all the required features).

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains six space-separated integers A, B, A1, B1, A2, B2.


Output Format:
For each test case, print a single line containing the integer 1 if Chef should switch to the first language, or 2 if Chef should switch to the second language, or 0 if Chef cannot switch to either language.

Constraints:
a. 1 ≤ T ≤ 288
b. 1 ≤ A, B, A1, B1, A2, B2 ≤ 4
c. A, B are distinct
d. A1, B1, A2, B2 are pairwise distinct

Sample Input 1:
3
1 2 2 1 3 4
3 4 2 1 4 3
1 2 1 3 2 4

Sample Output 1:
1
2
0

Explanation:
Example Case 1: The first language has the required features --- features 1 and 2.

Example Case 2: The second language has the required features --- features 3 and 4.

Example Case 3: Neither language has both features 1 and 2.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read six space-separated integers (here, features)
  A, B, A1, B1, A2, B2 = map(int, input().split())
  
  # check conditions
  if (A == A1 and B == B1) or (A == B1 and B == A1) :
    print('1')
  elif (A == A2 and B == B2) or (A == B2 and B == A2) :
    print('2')
  else :
    print('0')