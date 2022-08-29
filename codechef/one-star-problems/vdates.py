# Problem Name : Vaccine Dates

"""
Problem Statement:
Chef has taken his first dose of vaccine D days ago. He may take the second dose no less than L days and no more than R days since his first dose.

Determine if Chef is too early, too late, or in the correct range for taking his second dose.

Input Format:
a. First line will contain T, number of testcases. Then the testcases follow.
b. Each testcase contains of a single line of input, three integers D,L,R.


Output Format:
For each test case, print a single line containing one string - "Too Early" (without quotes) if it's too early to take the vaccine, "Too Late" (without quotes) if it's too late to take the vaccine, "Take second dose now" (without quotes) if it's the correct time to take the vaccine.

Constraints:
a. 1 ≤ T ≤ 10^5
b. 1 ≤ D ≤ 10^9
c. 1 ≤ L ≤ R ≤ 10^9

Sample Input 1:
4
10 8 12 
14 2 10
4444 5555 6666 
8 8 12

Sample Output 2:
Take second dose now
Too Late
Too Early
Take second dose now

Explanation:
Test Case 1: The second dose needs to be taken within 8 to 12 days and since the Day 10 lies in this range, we can take the second dose now.

Test Case 2: The second dose needs to be taken within 2 to 10 days since Day 14 lies after this range, it is too late now.

Test Case 3: The second dose needs to be taken within 5555 to 6666 days and since the Day 4444 lies prior to this range, it is too early now.
"""

# cook your dish here

# read the number of test cases.
test_cases = int(input())

for test_case in range(test_cases):

  # read integer
  D, L, R = map(int, input().split())
  
  if D > R :
    print('Too Late')
  else :
    if (D < L) :
      print('Too Early')
    else :
      print('Take second dose now')