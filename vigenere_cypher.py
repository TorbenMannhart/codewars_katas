# not finished..
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alph = alphabet
        self.letter_to_number = {}
        self.number_to_letter = {}
        for i in range(len(alphabet)):
            self.letter_to_number[alphabet[i]] = i + 1
            self.number_to_letter[i+1] = alphabet[i]
        
    
    def encode(self, text):
        upper_case_log = self.upper_case_log(text)
        text = text.lower()
        text_in_numbers =  self.to_numbers_list(text)
        repeated_key = self.repeat_key(text)
        repeated_key_numbers = self.to_numbers_list(repeated_key)
        shifted_numbers = []
        for i in range(len(text_in_numbers)):
            shifted = text_in_numbers[i] + repeated_key_numbers[i]
            if shifted > 26:
                shifted_numbers.append(shifted - 27)
            else:
                shifted_numbers.append(shifted-1)

        res = self.to_string_list(shifted_numbers)
        res = [res[i].upper() if upper_case_log[i] == 1 else res[i] for i in range(len(res))]
        return ''.join(res)

    
    def decode(self, text):
        upper_case_log = self.upper_case_log(text)
        text = text.lower()
        text_in_numbers =  self.to_numbers_list(text)
        repeated_key = self.repeat_key(text)
        repeated_key_numbers = self.to_numbers_list(repeated_key)
        shifted_numbers = []
        for i in range(len(text_in_numbers)):
            shifted = text_in_numbers[i] - repeated_key_numbers[i]
            if shifted < 0:
                shifted_numbers.append(shifted + 27)
            else:
                shifted_numbers.append(shifted + 1)
        res = self.to_string_list(shifted_numbers)
        res = [res[i].upper() if upper_case_log[i] == 1 else res[i] for i in range(len(res))]
        return ''.join(res)

    def repeat_key(self, text):
        repeated_key = []
        for i in range(len(text)):
            while i >= len(self.key):
                i -= len(self.key)
            repeated_key.append(self.key[i])
        return repeated_key

    def to_numbers_list(self, text):
        return [self.letter_to_number[l] for l in text]

    def to_string_list(self, numbers):
        return [self.number_to_letter[n] for n in numbers]

    def upper_case_log(self, text):
        upper_case_log = []
        for l in text:
            if l.isupper():
                upper_case_log.append(1)
            else:
                upper_case_log.append(0)
        return upper_case_log





alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

# creates a cipher helper with each letter substituted
# by the corresponding character in the key
c = VigenereCipher(key, alphabet)

print(c.encode('codewars')) #  returns 'rovwsoiv'
print(c.decode('laxxhsj'))  # returns 'waffles'
print(c.encode('CODEWARS')) #  returns 'rovwsoiv'
print(c.encode('ROVWSOIV')) #  returns 'rovwsoiv'
print(c.decode(c.encode('CODEwARS'))) #  returns 'rovwsoiv'
