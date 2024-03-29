'''
John works at a clothing store. He has a large pile of socks
that he must pair by color for sale. Given an array of integers
representing the color of each sock, determine how many pairs
of socks with matching colors there are.

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock
'''
def sock_merchant(n, ar):
    res = map(lambda x: ar.count(x), set(ar))
    c = 0
    for s in res:
        while s > 1:
            s -= 2
            c += 1
    return c

num = 9
array = (10, 20, 20, 10, 10, 30, 50, 10, 20)

print(sock_merchant(num, array))
