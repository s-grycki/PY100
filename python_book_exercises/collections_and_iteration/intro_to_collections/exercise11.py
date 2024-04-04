# Consider the data in the following table:

# Name 	      Country
# Alice 	    USA
# Francois 	  Canada
# Inti 	      Peru
# Monika 	    Germany
# Sanyu 	    Uganda
# Yoshitaka 	Japan

# You need to write some Python code to determine the country name associated
# with one of the listed names. Your code should include the data structure(s)
# you need and at least one test case to ensure the code works.

# What jumps out to me is that this has associated data logic. That suggests
# the use of a map to connect keys with values. The only concern I would have
# is the possibility of duplicate names. This would overwrite keys/value pairs
# already in the collection. But the example doesn't account for this, so I'll
# assume all names will be unique

# Once the map(dictonary) is created, we just have to reference by key to get
# back a value

people = {
    'Alice':      'USA',
    'Francois':   'Canada',
    'Inti':       'Peru',
    'Monika':     'Germany',
    'Sanya':      'Uganda',
    'Yoshitaka':  'Japan',
}

print(people['Alice'])
