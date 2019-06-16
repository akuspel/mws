import string

def encode(text):
    letters = list(string.ascii_lowercase) + list(string.ascii_lowercase)
    x = ""
    for t in text.lower():
        if t in letters:
            x += (letters[ord(t) - 97 + 13])
        else:
            x += t
    return(x)