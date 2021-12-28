# first working solution
import string
def find_missing_letter(chars):
    alphabet = string.ascii_letters
    start = alphabet.index(chars[0])
    for i, char in enumerate(chars):
        if alphabet[i+start] != char:
            return alphabet[i+start]

# shorter version
def find_missing_letter(chars):
    alphabet = string.ascii_letters
    ind = alphabet.index(chars[0])
    return [alphabet[i+ind] for i, char in enumerate(chars) if alphabet[i+ind] != char][0]

# codewars best solution
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))


    

print(find_missing_letter(["a","b","c","d","f"])) # "e"
print(find_missing_letter(['O','Q','R','S'])) # 'P'
