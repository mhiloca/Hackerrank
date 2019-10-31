from collections import Counter
from operator import itemgetter

s = input()
res = sorted(Counter(s).items())
final = sorted(res, key=itemgetter(1), reverse=True)
for i in range(3):
    print(final[i][0], final[i][1])
