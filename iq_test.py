"""
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""
# first working solution
def iq_test(numbers):
    m = [int(i) % 2 for i in numbers.split(' ')]
    if sum(m) == 1:
        return m.index(1) + 1
    else:
        return m.index(0) + 1

# codewars solution
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

# more efficient solution
def iq_test(numbers):
    m = [int(i) % 2 for i in numbers.split(' ')]
    if sum(m[0:3]) <= 1:
        return m.index(1) + 1
    else:
        return m.index(0) + 1

# even more efficient (not yet working)
# def iq_test(numbers):
#     d = True
#     num = numbers.split()
#     m = [int(num[0])]
#     while d == True:
#         for i, n in enumerate(num[1:]):
#             if int(n) % 2 != int(num[i-1]) % 2:
#                 m.append(int(n) % 2)
#                 d = False
#     print(m)
#     if sum(m[0:3]) <= 1:
#         return m.index(1) + 1
#     else:
#         return m.index(0) + 1



a = "2 4 7 8 10"    # 3
b = "1 2 1 1"       # 2
c = "1 2 2 2"       # 1
d =  '13 17 49 13 25 15 15 3 9 13 5 23 47 28'
print(iq_test(a))
print(iq_test(b))
print(iq_test(c))
print(iq_test(d))