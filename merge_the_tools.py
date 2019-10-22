"""
Consider the following:
A string, s, of n length  where s = c[0], c[1] ... c[n-1].
An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, t , consists of a
contiguous block of k characters in s. Then, use each t to create string u such that:
The characters in u are a subsequence of the characters in t.
Any repeat occurrence of a character is removed from the string such that each
character in u occurs exactly once. In other words, if the character at
some index j in t occurs at a previous index <j in t, then do not include
the character in string u.
Given s and k, print n/k lines where each line i denotes string u.
Input Format
The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.
"""
def merge_the_tools(string, k):
    n = list(string)
    lines = len(n) // k
    for i in range(lines):
        c, sub = 0, []
        while c < k and n:
            s = n.pop(0)
            if s not in sub:
                sub.append(s)
            c += 1
        print(''.join(sub))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


