import re

def solve(s):
    check = re.compile(re.compile(r'^[0-9]'))
    names = s.split(' ')
    return ' '.join(name if check.match(name) else name.capitalize() for name in names)


print(solve('hello   world  lol'))