n, m = map(int, input().split())
d = '.|.'
l = n//2
for i in range(0, l):
    if i < n //2:
        print((d*(i+(i+1))).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(n, -1, -2):
    if n != i and i % 2 != 0:
        print((d*(i)).center(m, '-'))
    elif i == 0:
        print(d.center(m, '-'))