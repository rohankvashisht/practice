# Problem Name : Weight Balance

"""
Problem Statement:
No play and eating all day makes your belly fat. This happened to Chef during the lockdown. His weight before the lockdown was w1 kg (measured on the most accurate hospital machine) and after M months of lockdown, when he measured his weight at home (on a regular scale, which can be inaccurate), he got the result that his weight was w2 kg (w2>w1).

Scientific research in all growing kids shows that their weights increase by a value between x1 and x2 kg (inclusive) per month, but not necessarily the same value each month. Chef assumes that he is a growing kid. Tell him whether his home scale could be giving correct results.

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains five space-separated integers w1, w2, x1, x2 and M.


Output Format:
For each test case, print a single line containing the integer 1 if the result shown by the scale can be correct or 0 if it cannot.

Constraints:
a. 1 ≤ T ≤ 10^5
b. 1 ≤ w1 < w2 ≤ 100
c. 1 ≤ x1 < x2 ≤ 10
d. 1 ≤ M ≤ 10

Sample Input 1:
5
1 2 1 2 2
2 4 1 2 2
4 8 1 2 2
5 8 1 2 2
1 100 1 2 2

Sample Output 1:
0
1
1
1
0

Explanation:
Example Case 1: Since the increase in Chef's weight is 2 - 1 = 1 kg and that is less than the minimum possible increase 1 * 2 = 2 kg, the scale must be faulty.

Example Case 2: Since the increase in Chef's weight is 4 - 2 = 2 kg, which is equal to the minimum possible increase 1 * 2 = 2 kg, the scale is showing correct results.

Example Case 3: Since the increase in Chef's weight is 8 - 4 = 4 kg, which is equal to the maximum possible increase 2 * 2 = 4 kg, the scale is showing correct results.

Example Case 4: Since the increase in Chef's weight is 8 - 5 = 3 kg lies in the interval [1*2, 2*2] kg, the scale is showing correct results.

Example Case 5: Since the increase in Chef's weight is 100 - 1 = 99 kg and that is more than the maximum possible increase 2 * 2 = 4 kg, the weight balance must be faulty.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read integers
  w1, w2, x1, x2, M = map(int, input().split())
  
  # scale difference in lockdown
  weight_change = w2-w1 
  
  if (weight_change >= x1 * M ) and (weight_change <= x2 * M) :
    print(1)
  else :
    print(0)
  