# Problem Name : Programming Languages

"""
Problem Statement:
Chef is playing Need For Speed. Currently, his car is running on a straight road with a velocity U metres per second and approaching a 90∘ turn which is S metres away from him. To successfully cross the turn, velocity of the car when entering the turn must not exceed V metres per second.

The brakes of Chef's car allow him to slow down with a deceleration (negative acceleration) not exceeding A metres per squared second. Tell him whether he can cross the turn successfully. The velocity v when entering the turn can be determined from Newton's 2nd law to be v^2=U^2+2*a*S the car is moving with a uniform acceleration a.

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first and only line of each test case contains four space-separated integers U, V, A and S.


Output Format:
For each test case, print a single line containing the string "Yes" if Chef can cross the turn successfully or "No" if he cannot (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints:
a. 1 ≤ T ≤ 10^5
b. 1 ≤ U, V, A, S ≤ 10^4

Sample Input 1:
3
1 1 1 1
2 1 1 1
2 2 1 1

Sample Output 1:
Yes
No
Yes

Explanation:
Example Case 1: Since U = V = 1, Chef does not need to brake and will be able to turn successfully.

Example Case 2: The smallest velocity Chef's car can have even with the maximum deceleration is (2*2 - 2*1*1)^(1/2) = (2)^(1/2), which is greater than the maximum allowed velocity for a safe turn.

Example Case 3: The smallest velocity Chef's car can have with the maximum deceleration is again 2^(1/2), which is smaller than the maximum allowed velocity for a safe turn.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read initial, final velocities, acceleration and displacement
  U, V, A, S = map(int, input().split())
  v2 = (U**2) - (2*A*S)
  
  # check conditions
  if U >= V :
    if U > V :
      if (v2) <= (V**2) :
        print('Yes')
      else :
        print ('No')
    else :
      print('Yes')
  else :
    print('Yes')