from itertools import combinations

n = int(input())
s = input().split()
k = int(input())

c = list(combinations(s, k))
f = list(filter(lambda x: 'a' in x, c))
print(len(f)/len(c))
