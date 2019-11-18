import re

def repeated_sub(s):
    pattern = re.compile(r'([a-zA-Z0-9])')
    for i, el in enumerate(s):
        if i > 0 and el == s[i-1]:
            if pattern.match(el):
                return el
    return -1

string = input()
print(repeated_sub(string))