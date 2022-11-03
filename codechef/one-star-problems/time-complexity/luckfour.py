# Problem Name : Lucky Four

"""
Problem Statement:
Kostya likes the number 4 much. Of course! This number has such a lot of properties, like:

a. Four is the smallest composite number;
b. It is also the smallest Smith number;
c. The smallest non-cyclic group has four elements;
d. Four is the maximal degree of the equation that can be solved in radicals;
e. There is four-color theorem that states that any map can be colored in no more than four colors in such a way that no two adjacent regions are colored in the same color;
f. Lagrange's four-square theorem states that every positive integer can be written as the sum of at most four square numbers;
g. Four is the maximum number of dimensions of a real division algebra;
h. In bases 6 and 12, 4 is a 1-automorphic number;
i. And there are a lot more cool stuff about this number!

Impressed by the power of this number, Kostya has begun to look for occurrences of four anywhere. He has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit 4 in the decimal representation. He is too busy now, so please help him.

Input:
The first line of input consists of a single integer T, denoting the number of integers in Kostya's list.
Then, there are T lines, each of them contain a single integer from the list.

Output:
Output T lines. Each of these lines should contain the number of occurences of the digit 4 in the respective integer from Kostya's list.

Constraints:
a. 1 ≤ T ≤ 10^5
b. (Subtask 1): 0 ≤ Numbers from the list ≤ 9 - 33 points.
c. (Subtask 2): 0 ≤ Numbers from the list ≤ 109 - 67 points.


Sample Input:
5
447474
228
6664
40
81

Sample Output:
4
0
1
1
0
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):

  number_of_fours = 0

  number = int(input())

  while (number) :
    
    if((number%10) == 4) :
      number_of_fours += 1
    
    number = int(number/10)
  
  print(number_of_fours)