# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# The first function call prints 'Product2'. This is because the passed
# argument matches an explicitly given case

# The second function call prints 'Product not found!'. This is because the
# passed argument of 142 doesn't match any of the cases provided
