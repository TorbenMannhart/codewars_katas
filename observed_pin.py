"""
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

return list of all possible pins with a given input pin 
each input digit could also be the number next, above or below it (see numberpad)
"""
# first working solution
import itertools
def get_pins(observed):
    adjacent = {
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8'],
        '0': ['0', '8']
    }
    r = list(itertools.product(*[adjacent[v] for v in observed]))
    return [''.join(i) for i in r]
    
# shorter solution
def get_pins(observed):
    adjacent = {
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8'],
        '0': ['0', '8']
    }
    r = list(itertools.product(*[adjacent[v] for v in observed]))
    return  [''.join(i) for i in r]





a = get_pins('8') # ['5','7','8','9','0']
b = get_pins('369') # ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]


print(a)
print(b)
