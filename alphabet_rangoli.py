def print_rangoli(n):
    x = (n * 2) - 2
    l = 0
    al = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(x, -1, -2):
        c = n
        l += 1
        print('-' * i, end='')
        for j in range(l):
            print(al[c-1], end='-') if i != x else print(al[c-1], end='')
            c -= 1
            if c - 1 < 0:
                break
        if i < x:
            d = c
            for j in range(l-1):
                d += 1
                print(al[d], end='-') if d != n-1 else print(al[d], end='')
                if d > n:
                    break
        print('-' * i)
    l = n
    for i in range(2, x+1, 2):
        c = n
        l -= 1
        print('-' * i, end='')
        for j in range(l):
            print(al[c-1], end='-')
            c -= 1
        d = c+1
        for j in range(l-1):
            print(al[d], end='-') if d != n - 1 else print(al[d], end='')
            d += 1
        print('-' * i) if i != x else print('-' * (i-1))

n = int(input())
print_rangoli(n)