"""
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north 
and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, 
therefore, the final result is []
"""
# first working solution
def dirReduc(arr):
    opp = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH','EAST': 'WEST','WEST': 'EAST'}
    r = []
    for d in arr:
        if r == [] or d != opp[r[-1]]:
            r.append(d)
        else:
            del r[-1]
    if r != arr:
        return dirReduc(r)
    return r

# codewars solution (altered by me: added 'dummy' to new_plan, otherwise loop has to check if empty every time):
def dirReduc(plan):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    new_plan = ['dummy']
    for d in plan:
        if new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan[1:] # remove dummy



a = ["NORTH", 'NORTH', "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] 
b = ["NORTH", "WEST", "SOUTH", "EAST"]
c = ["NORTH", "EAST", "WEST", "SOUTH"]

print(dirReduc(a)) # ["WEST"]
print(dirReduc(b)) # ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(c)) # []