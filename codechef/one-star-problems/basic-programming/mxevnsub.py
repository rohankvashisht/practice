# Problem Name : Maximum Length Even Subarray

"""
Problem Statement:
You are given an integer N. Consider the sequence containing the integers 1,2,…,N in increasing order (each exactly once). Find the maximum length of its contiguous subsequence with an even sum.

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains a single integer N.


Output Format:
For each test case, print a single line containing one integer --- the maximum length of a contiguous subsequence with even sum.

Constraints:
a. 1 ≤ T ≤ 10^4
b. 2 ≤ N ≤ 10^4

Sample Input 1:
3
3
4
5

Sample Output 1:
3
4
4

Explanation:
Example Case 1: The optimal choice is to choose the entire sequence, since the sum of all its elements is 1+2+3=6, which is even.

Example Case 3: One of the optimal choices is to choose the subsequence [1,2,3,4], which has an even sum.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read integer
  N = int(input())
  
  # sum of m natural numbers
  def sum_of_m(m):
    return int((m*(m+1))/2)

  if (sum_of_m(N) % 2) == 0 :
    print(N)
  else :
    # contiguous sequence excluding number 1
    print(N-1)
  