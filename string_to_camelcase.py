import re
# first working solution
def to_camel_case(text):
    words = re.split('-|_', text)
    res = words[0]
    print(words)
    for word in words[1:]:
        res = res + word.capitalize()
    return res

def to_camel_case(text):
    return ''.join([w.capitalize() if i != 0 else w for i, w in enumerate(re.split('-|_', text))])


print(to_camel_case('hello-world_hello'))



