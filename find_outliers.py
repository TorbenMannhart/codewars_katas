# def find_outlier(integers):
#     l = [i%2 for i in integers]
#     if sum(l) > 1:
#         print([integers[i] for i, val in enumerate(l) if val == 0][0])
#     else:
#         print([integers[i] for i, val in enumerate(l) if val != 0][0])

def find_outlier(integers):
    l = [i%2 for i in integers]
    return integers[next(i for i, val in enumerate(l) if val == (0 if sum(l) > 1 else 1))]



x = find_outlier([160, 7, 3, 9, 17])
y = find_outlier([2, 4, 8, 17, 122])

print(x)
print(y)


# [0, 1, 1, 1, 1]
# [0, 0, 0, 1, 0]