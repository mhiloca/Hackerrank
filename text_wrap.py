def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        try:
            print(string[i:i+max_width])
        except:
            print(string[i:])

s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w = 4

wrap(s, w)