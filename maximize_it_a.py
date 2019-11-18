from itertools import product

k, m = map(int, input().split())
n = []
for i in range(k):
    c = list(map(int, input().split()))
    n.append(c[1:])
p = list(product(*n))
s = []
for i in p:
    s.append((sum(map(lambda x: x * x, i)))%m)
print(max(s))