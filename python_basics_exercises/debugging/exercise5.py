# You want to have a small script delivering motivational quotes,
# but with the following code you run into a very common error message:
# TypeError: can only concatenate str (not "NoneType") to str.
# What is the problem and how can you fix it?

def get_quote(person):
    if person == 'Yoda':
        'Do. Or do not. There is no try.'
    if person == 'Confucius':
        'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

# print('Confucius says:')
# print('"' + get_quote('Confucius') + '"')



# In Python, a function returns None by default unless an explicit return is
# defined. With this function, all 3 if conditionals will evaluate. Even
# though the if block tied to confucious will evaluate, nothing is done with
# it and the code continues with a None return. To fix this, we simply need to
# return the string. Also, this could be refactored into an if/else block or a
# match/case block. I think match, since we're simply evaluating the value of
# a passed string

def get_quote(person):
    match person:
        case 'Yoda':
            return 'Do. Or do not. There is no try.'
        case 'Confucius':
            return ('I hear and I forget. I see and I remember. ' 
            'I do and I understand.')
        case 'Einstein':
            return ('Do not worry about your difficulties in Mathematics. '
            'I can assure you mine are still greater.')

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
