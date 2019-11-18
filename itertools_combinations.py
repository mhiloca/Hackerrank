from itertools import combinations, combinations_with_replacement

s = input().split()

for i in range(int(s[1])):
    for j in combinations(sorted(s[0]), i+1):
        print(''.join(j))

print('- ' * 15)
for i in combinations_with_replacement(sorted(s[0]), int(s[1])):
    print(''.join(i))