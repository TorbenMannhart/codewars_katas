# first working solution
import itertools
def permutations(string):
    p = list(dict.fromkeys(itertools.permutations(string, len(string))))
    return [''.join(i) for i in p]

# codewars solution
def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


a = permutations('a'); # ['a']
b = permutations('ab'); # ['ab', 'ba']
c = permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

print(a)
print(b)
print(c)