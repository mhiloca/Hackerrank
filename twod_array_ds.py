from random import randint

def hourglass_sum(arr):
    # minimum hourglass sum = -9 * 7 = -63
    maxSum = -63

    for i in range(4):
        for j in range(4):

            top = sum(arr[i][j:j+3])

            mid = sum(arr[i+1][j+1])

            bottom = sum(arr[i+2][j:j+3])

            hg = top + mid + bottom

            if hg > maxSum:
                maxSum = hg

    return maxSum


def cal_hg(arr, i, j):
    return sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])


def hourglass_sum_a(arr):
    valores = [cal_hg(arr, l, c) for l in range(4) for c in range(4)]
    return max(valores)


array = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

# print(hourglass_sum_a(array))

def show_array_start(arr):
    for l in range(len(arr)-2):
        for c in range(len(arr)-2):
            print('Starting position: ', l, c)

show_array_start(array)
