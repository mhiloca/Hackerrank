'''
Complete the repeatedString function in the editor below.
It should return an integer representing the number of occurrences
of a in the prefix of length n in the infinitely repeating string.
repeatedString has the following parameter(s):
s: a string to repeat
n: the number of characters to consider
'''
def repeated_string(s, n):
    if s == 'a':
        return n
    return s.count('a') * int(n/len(s)) + s[:n%len(s)].count('a')

print(repeated_string('aba', 10))

