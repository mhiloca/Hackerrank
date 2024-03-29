'''
Consider the following problem:
Write a short program that prints each number from 1 to 100 on a new line.

For each multiple of 3, print "Fizz" instead of the number.

For each multiple of 5, print "Buzz" instead of the number.

For numbers which are multiples of both 3 and 5, print "FizzBuzz"
instead of the number.
Write a solution (or reduce an existing one) so it has as few
characters as possible.
'''
for i in range(1, 101):
    if i % 3 == 0:
        print('FizzBuzz' if i % 5 == 0 else 'Fizz')
    else:
        print('Buzz' if i % 5 == 0 else i)
