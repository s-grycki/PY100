# Refactor this statement to use a regular if statement instead.

return ('bar' if foo() else qux())

if foo():
    return 'bar'
else:
    return qux()

# This seems like bad practice to me. We're returning a string based on the
# truthiness value of a function call, or returning the value of a different
# function call if the original function call was falsy. This would get
# confusing very quickly in a larger program. The rewrite to an if statement
# does add some readability, but it's still fragile and would be better with
# the desired return logic exported out to the respective functions, and
# calling one of 2 functions based on a simple evaluation
