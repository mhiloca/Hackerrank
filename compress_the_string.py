from itertools import groupby

s = input()
# g = (x for x in s)
for i, g in groupby(s, ):
    print((len(list(g)), int(i)), end=' ')
# print(dir(groupby(s)))

