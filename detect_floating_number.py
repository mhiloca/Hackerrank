import re

def check_float(n):
    pattern = re.compile(r'^[+\-]?[0-9]*\.[0-9]+$')
    if pattern.match(n) or type(n) == int:
        return True
    return False

n = int(input())
nums = []
for i in range(n):
    nums.append(input().strip())
for num in nums:
    print(check_float(num))