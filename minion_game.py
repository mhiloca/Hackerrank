"""
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string S.
For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points
"""


def minion_game(string):
    vowels = 'AEIOU'
    kevin = stuart = 0
    for cont in range(len(string)):
        if string[cont] in vowels:
            kevin += len(string) - cont
        else:
            stuart += len(string) - cont
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif kevin == stuart:
        print('Draw')
    else:
        print(f'Stuart {stuart}')



def minion_game_v2(s):
    vowels = 'AEIOU'
    kev = stu = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kev += (len(s) - i)
        else:
            stu += (len(s) - i)
    if kev > stu:
        print("Kevin", kev)
    elif kev < stu:
        print("Stuart", stu)
    else:
        print("Draw")


s = input().strip().upper()
minion_game(s)