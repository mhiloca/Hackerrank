n = int(input())
students = [[input(), float(input())] for i in range(n)]
scores = sorted({s[1] for s in students})
sec_lower = sorted(x[0] for x in students if x[1] == scores[1])
print('\n'.join(sec_lower))



