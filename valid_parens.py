"""
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""
# first working solution
def valid_parentheses(string):
    dc  = {'(': 1, ')': -1}
    r = 0
    for i in [dc[p] for p in string if p == '(' or p == ')']:
        r += i
        if r <0:
            return False
    return r == 0


print(valid_parentheses('')) # True
print(valid_parentheses('()')) # True
print(valid_parentheses("hi())(")) # False