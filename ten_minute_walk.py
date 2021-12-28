""" each direction is walking 1 min in this direction (n, e, s ,w)  in the end you it has to take ten minutes and bring you back to your starting point"""
# first working solution
def is_valid_walk(walk):
    sum_lat = 0
    sum_vert = 0
    if len(walk) == 10:
        for d in walk:
            if d == 'n':
                sum_lat += 1
            if d == 's':
                sum_lat -= 1
            if d == 'e':
                sum_vert += 1
            if d == 'w':
                sum_vert -= 1
        return sum_lat == 0 and sum_vert == 0
    return False

# shorter form
def is_valid_walk(walk):
    dc = {'n':0, 'w':0, 's': 0, 'e':0}
    for d in walk:
        dc[d] +=1
    return dc['n']-dc['s'] == 0 and dc['w']-dc['e'] == 0 and len(walk) == 10


# even shorter, but slower (looping through list 4 times instead of 1) (not mine) 
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
def is_valid_walk(walk):
    return walk.count('n') + walk.count('e') == 5 and walk.count('n') == walk.count('s')


print(is_valid_walk(['n', 'n', 'e', 's', 's', 's', 's', 'w', 'n', 'n'])) # True
print(is_valid_walk(['s', 'n', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'])) # False
print(is_valid_walk(['s', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'])) # False
print(is_valid_walk(['n', 'n', 's', 's'])) # False