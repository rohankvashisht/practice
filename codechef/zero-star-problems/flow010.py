# Problem Name : Id and Ship

"""
Problem Statement:
Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.
Class ID  Ship Class
B or b  BattleShip
C or c	Cruiser
D or d	Destroyer
F or f	Frigate

Input:
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains a character.    

Output:
For each test case, display the Ship Class depending on ID, in a new line.

Constraints:
a. 1 ≤ T ≤ 1000

Sample Input:
3
B
c
D

Sample Output:
BattleShip
Cruiser
Destroyer
"""

# cook your dish here

# read the number of test cases
test_cases = int(input())

for test_case in range(test_cases):
  class_id = input().lower()

  if (class_id == 'b') :
    print('BattleShip')
  elif (class_id == 'c') :
    print('Cruiser')
  elif (class_id == 'd') :
    print('Destroyer')
  elif (class_id == 'f') :
    print('Frigate')
  else :
    print('Invalid input')

  
  