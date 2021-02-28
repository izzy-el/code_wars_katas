import string

def is_pangram(s):
    alphabet = string.ascii_lowercase
    s.lower()
    for i in alphabet:
        if(i not in s):
            return False
    return True