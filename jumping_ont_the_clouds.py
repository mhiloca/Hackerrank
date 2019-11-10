'''
Emma is playing a new mobile game that starts with consecutively
numbered clouds. Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to the
number of the current cloud plus 1 or 2. She must avoid the thunderheads.
Determine the minimum number of jumps it will take Emma to jump from her
starting position to the last cloud. It is always possible to win the game.
Print the minimum number of jumps needed to win the game.
'''
def jumping_on_clouds(c):
    i = j = 0
    while i < len(c):
        if i+2 < len(c) and c[i+2] == 0:
            i += 1
            j += 1
        else:
            if i+1 < len(c) and c[i+1] == 0:
                j += 1
        i += 1
    return j

print(jumping_on_clouds((0, 0, 1, 0, 0, 1, 0)))