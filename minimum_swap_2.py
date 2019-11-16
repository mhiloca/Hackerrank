def minimumSwaps(arr):
    array = [n-1 for n in arr]
    swap = 0
    while array != sorted(array):
        for i, n in enumerate(array):
            if n != i:
                array[array.index(i)] = n
                array[i] = i
                swap += 1
                break
    return swap

# More efficient solution - less time because uses ony one loop and doesn't
# call for arr.index()
def minimun_swaps(arr):
    swap = 0
    indexes = {el: i for i, el in enumerate(arr)}
    for i in range(len(arr), 0, -1):
        if i != arr[i-1]:
            index = indexes[i]
            indexes[i] = i - 1
            indexes[arr[i-1]] = index
            arr[i-1], arr[index] = arr[index], arr[i-1]
            swap += 1
    return swap

array = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(array))
