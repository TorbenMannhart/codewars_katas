
x = 4
from itertools import combinations_with_replacement
def enum(n):
    for i in range(1, n+1):
        for comb in combinations_with_replacement([i for i in range(1,n+1)], i):
            if sum(comb) != n:
                continue
            else:
                yield [i for i in comb if i != 0]


for result in enum(x):
    print(result)

print('-'*50)

def enum(n):
    for i in range(1, n):
        for comb in combinations_with_replacement([i for i in range(1,n)], i):
            if sum(comb) != n:
                continue
            else:
                yield comb

for result in enum(x):
    print(result)