# Write a function, even_or_odd, that determines whether its argument is an
# even or odd number. If it's even, the function should print 'even';
# otherwise, it should print 'odd'. Assume the argument is always an integer.

# Using a ternary expression (most terse)
def even_or_odd(num):
    print('even' if num % 2 == 0 else 'odd')

even_or_odd(5)
even_or_odd(4)



# Using if/else statement (most read-able)
def even_or_odd(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

even_or_odd(5)
even_or_odd(4)



# Using match statement (most logic)
def even_or_odd(num):
    num = bool(num % 2 == 0)

    match num:
        case True:
            print('even')
        case _:
            print('odd')

even_or_odd(5)
even_or_odd(4)
