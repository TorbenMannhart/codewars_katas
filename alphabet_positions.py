def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join([str(alphabet.index(i)+1) for i in text.lower() if i in alphabet])


res = alphabet_position("abcdefg h ") # "1 2"

print(res)