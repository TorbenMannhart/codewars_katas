


def is_square(n):
    return n >= 0 and int(n**(0.5))**2 == n 


print(is_square(4)) # True
print(is_square(3)) # False
print(is_square(-1)) # False
print(is_square(0)) # False
print(is_square(25)) # True
print(is_square(9999999999999999))