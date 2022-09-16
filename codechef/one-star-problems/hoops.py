# Problem Name : Hoop Jump

"""
Problem Statement:
You and your friend are playing a game with hoops. There are N hoops (where N is odd) in a row. You jump into hoop 1, and your friend jumps into hoop N. Then you jump into hoop 2, and after that, your friend jumps into hoop N-1, and so on.

The process ends when someone cannot make the next jump because the hoop is occupied by the other person. Find the last hoop that will be jumped into.

Input Format:
a. First line will contain T, number of test cases. Then the test cases follow.
b. Each test case contains a single line of input, a single integer N.


Output Format:
For each testcase, output in a single line the answer to the problem.

Constraints:
a. 1 ≤ T ≤ 10^5
b. 1 ≤ N ≤ 2 * 10^5
c. N is odd

Sample Input 1:
2
1
3

Sample Output 1:
1
2

Explanation:
Test Case 1: Since there is only 1 hoop, that's the only one to be jumped into.

Test Case 2: The first player jumps into hoop 1. The second player jumps into hoop 333 and finally the first player jumps into hoop 2. Then the second player cannot make another jump, so the process stops.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # total number of hoops in a row (provided it is odd)
  length_of_hoops = int(input())
  
  # print the middle hoop number
  print((length_of_hoops+1)/2)