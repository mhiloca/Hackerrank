import re

def vowels_two_more(s):
    pattern = re.compile(r'([aeiouAEIOU]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+')
    return '\n'.join(pattern.findall(s))

string = 'abaabaabaabaae'
print(vowels_two_more(string))

