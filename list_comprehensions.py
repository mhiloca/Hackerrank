a, b, c, n = input().split()
a, b, c, n = int(a), int(b), int(c), int(n)
print([[i, j, k]
       for i in range(a+1)
       for j in range(b+1)
       for k in range(c+1)
       if i+j+k != n])

