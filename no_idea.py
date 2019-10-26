x, y = input().split()
n = list(input().split())
a = set(input().split())
b = set(input().split())
total = 0
for i in n:
    if i in a:
        total += 1
    elif i in b:
        total -= 1
print(total)