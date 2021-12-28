"""
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

"""
942 -> 9+4+2
"""
# first working solution
def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        return digital_root(sum(int(d) for d in str(n)))

# shorter solution
def digital_root(n):
    return n if n < 10 else digital_root(sum(int(d) for d in str(n)))

# one of codewars solution 
"""
The digital root of a number is equal to the remainder when that number is divided by 9. 
If the remainder is 0 and the number is greater than 0, then the digital root is 9. 
If the number is 0, then the digital root of the number is 0.
"""
def digital_root(n):
    return n%9 or n and 9 


print(digital_root(6)) # 6
print(digital_root(16)) # 7
print(digital_root(942)) # 6
