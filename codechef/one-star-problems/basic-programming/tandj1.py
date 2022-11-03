# Problem Name : Tom And Jerry 1

"""
Problem Statement:
There is a grid of size 10^5 x 10^5, covered completely in railway tracks. Tom is riding in a train, currently in cell (a,b), and Jerry is tied up in a different cell (c,d), unable to move. The train has no breaks. It shall move exactly K steps, and then its fuel will run out and it shall stop. In one step, the train must move to one of its neighboring cells, sharing a side. Tom can't move without the train, as the grid is covered in tracks. Can Tom reach Jerry's cell after exactly K steps?

Note: Tom can go back to the same cell multiple times.

Input Format:
a. The first line contains an integer T, the number of test cases. Then the test cases follow.
b. Each test case contains a single line of input, five integers a,b,c,d,K.


Output Format:
For each testcase, output in a single line "YES" if Tom can reach Jerry's cell in exactly K moves and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints:
a. 1 ≤ T ≤ 10^5
b. 0 ≤ a,b,c,d ≤ 10^5
c. (a,b) != (c,d)
d. 1 ≤ K ≤ 2*10^5

Sample Input 1:
3
1 1 2 2 2
1 1 2 3 4
1 1 1 0 3

Sample Output 1:
YES
NO
YES

Explanation:
Test Case 1: A possible sequence of moves is (1,1)→(1,2)→(2,2).

Test Case 2: There is a possible sequence in 3 moves, but not in exactly 4 moves.

Test Case 3: A possible sequence of moves is (1,1)→(1,0)→(0,0)→(1,0).
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  
  # read 4 coordinates and steps
  a, b, c, d, K = map(int, input().split())
  
  # calculate distance
  distance = abs(c-a) + abs(d-b)
  
  if (distance < K) and ((K - distance)%2 == 0) :
    print('YES')
  elif (distance == K) :
    print('YES')
  else :
    print('NO')
  