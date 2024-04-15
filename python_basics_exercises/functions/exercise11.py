# Building on your solutions from the previous exercises,
# write a function local_greet that takes a locale as input,
# and returns a greeting. The locale lets us greet people from different
# countries appropriately, even when they share a common language

# When implementing local_greet, make sure you re-use your extract_language,
# extract_region, and greet functions from the previous exercises

CONV_MAP = {
    'US': 'Hey!',
    'GB': 'Hello!',
    'AU': 'Howdy!',
    'fr': 'Salut!',
    'pt': 'Olá!',
    'de': 'Hallo!',
    'sv': 'Hej!',
    'af': 'Haai!',
}

def extract_language(locale):
    return locale[:2]

def extract_region(locale):
    return locale[3:5]

def greet(codes):
    for code in codes:
        if code in CONV_MAP.keys():
            return CONV_MAP[code]
        else:
            continue
    return 'Invalid code'

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    return greet((language, region))
    

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
print(local_greet('xx_XX.UTF-8'))       # Invalid code
