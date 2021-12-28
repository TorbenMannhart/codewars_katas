# my solution
def likes(names):
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    return f'{names[0]}, {names[1]} and {len(names)-2} others like this'

# best practice solution
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


a = likes([])
b = likes(['Peter'])
c = likes(['Jacob', 'Alex'])
d = likes(['Max', 'John', 'Mark'])
e = likes(['Alex', 'Jacob', 'Mark', 'Max'])

print(a)
print(b)
print(c)
print(d)
print(e)