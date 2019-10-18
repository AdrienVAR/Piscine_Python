import string

def n_lower_chars(string):
    return sum(map(str.islower, string))

def n_upper_chars(string):
    return sum(map(str.isupper, string))

def n_space_chars(string):
    return len(string.split(' '))

def n_punct_chars(string1):
    i = 0
    for c in string1:
        if c in string.punctuation:
            i += 1
    return (i)

def text_analyzer(string):
    print("The text contains", len(string) ,"characters:")
    print("-", n_lower_chars(string), "lower letters")
    print("-", n_upper_chars(string), "upper letters")
    print("-", n_punct_chars(string), "punctuations")
    print("-", n_space_chars(string), "spaces")
