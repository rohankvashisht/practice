# Problem Name : Smallest Possible Whole Number

"""
Problem Statement:
You are given two integers N and K. You may perform the following operation any number of times (including zero): change N to N-K, i.e. subtract K from N. Find the smallest non-negative integer value of N you can obtain this way.

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains two space-separated integers N and K.


Output Format:
For each test case, print a single line containing one integer — the smallest value you can get.

Constraints:
a. 1 ≤ T ≤ 10^5
b. 1 ≤ N ≤ 10^9
c. 1 ≤ K ≤ 10^9

Sample Input 1:
3
5 2
4 4
2 5

Sample Output 1:
1
0
2

Explanation:
Example Case 1:
a. First, we change N = 5 to N - K = 5 -2 = 3.
b. Then, we have N = 3 and we change it to N - K = 3 -2 = 1.

Since 1 < K, the process stops here and the smallest value is 1.

Example Case 2: We change N=4 to N - K = 4 - 4 = 0. Since 0 < K, the process stops here and the smallest value is 0.

Example Case 3: Since 2 < K initially, we should not perform any operations and the smallest value is 2.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read integer and it's subtractor
  N, K = map(int, input().split())
  
  if (K > 0) :
    print(N % K)
  else :
    print(N)