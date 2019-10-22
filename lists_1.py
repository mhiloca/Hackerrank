"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding
operation on your list.
Input Format
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.
Constraints
The elements added to the list must be integers.
Output Format
For each command of type print, print the list on a new line.
"""
from random import choice, randint


l = []
N = int(input())
for i in range(N):
    n = input().split()
    if n[0] == 'insert':
        l.insert(int(n[1]), int(n[2]))
    elif n[0] == 'print':
        print(l)
    elif n[0] == 'remove':
        l.remove(int(n[1]))
    elif n[0] == 'append':
        l.append(int(n[1]))
    elif n[0] == 'sort':
        l.sort()
    elif n[0] == 'pop':
        l.pop()
    elif n[0] == 'reverse':
        l.reverse()



