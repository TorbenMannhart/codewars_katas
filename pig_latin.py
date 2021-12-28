"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.
"""

def pig_it(text):
    return ' '.join([w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split(' ')])

print(pig_it('Pig latin is cool !')) # igPay atinlay siay oolcay !