def minimumBribes(q):
    bribes = 0
    for i, bri in enumerate(q):
        if (bri-1) - i > 2:
            return 'Too chaotic'
        for j in range(max(bri-2, 0), i):
            if q[j] > (bri-1):
                bribes += 1
    return bribes



arr = [1, 2, 5, 3, 7, 8, 6, 4]

print(minimumBribes(arr))
