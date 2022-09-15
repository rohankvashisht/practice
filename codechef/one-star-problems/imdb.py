# Problem Name : Motivation

"""
Problem Statement:
Chef has been searching for a good motivational movie that he can watch during his exam time. His hard disk has X GB of space remaining. His friend has N movies represented with (S_i,R_i) representing (space required, IMDB rating). Help Chef choose the single best movie (highest IMDB rating) that can fit in his hard disk.

Input Format:
a. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
b. The first line of each test case contains two space-separated integers N and X.
c. N lines follow. For each valid i, the i-th of these lines contains two space-separated integers S_i and R_i.

Output Format:
For each test case, print a single line containing one integer - the highest rating of an IMDB movie which Chef can store in his hard disk.

Constraints:
a. 1 ≤ T ≤ 10
b. 1 ≤ N ≤ 5 * 10^4
c. 1 ≤ X ≤ 10^9
d. 1 ≤ S_i, R_i ≤ 10^9 for each valid i
e. X ≥ S_i, for atleast one valid i

Sample Input 1:
3
1 1
1 1
2 2
1 50
2 100
3 2
1 51
3 100
2 50

Sample Output 1:
1
100 
51

Explanation:
Example Case 1: Since there is only 111 movie available and requires space equivalent to the empty space in the hard disk, Chef can only obtain maximum IMDB rating of 1.

Example Case 2: Since out of the 2 available movies, both can fit in the free memory, we only care to take the one with higher rating, i.e, rating of max(50,100) = 100.

Example Case 3: Since out of the 3 available movies, only the first and the last movies fit in the free memory, we only care to take the one with higher rating amongst these 2, i.e, rating of max(51,50) = 51.
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):

  # read number of movies and available hard disk space
  N, X = map(int, input().split())

  max_rating = 0

  for i in range(N):
    # read disk space of a movie and it's IMDB rating
    S_i, R_i = map(int, input().split())

    if (R_i > max_rating and S_i <= X) :
      max_rating = R_i
    
  print(max_rating)

