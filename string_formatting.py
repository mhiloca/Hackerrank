def print_formatted(number):
    l = len(bin(number)[2:])
    for i in range(number+1):
        print(f'{str(i).rjust(l, " ")} {oct(i)[2:].rjust(l, " ")} {hex(i)[2:].upper().rjust(l, " ")} {bin(i)[2:].rjust(l, " ")}')
    return ''


print_formatted(17)
