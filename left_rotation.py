def rotLeft(a, d):
    res = list(map(str, a))
    for i in range(d):
        aux = res.pop(0)
        res.append(aux)
    return ' '.join(res)

n = 10
arr = [41, 73, 89, 7, 10, 1,
       59, 58, 84, 77, 77, 97,
       58, 1, 86, 58, 26, 10, 86, 51]
print(rotLeft(arr, n))
