# Examine the code shown below. Without running it,
# determine what it will print

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

# It will print 'neigh' because the value pointed to by the animal variable
# equates to 'horse'.
