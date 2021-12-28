"""
input:  ordered list of integers
output: list of integers (if not in a range) or ranges from input list, where a range is denoted by a '-' and range must have at least length 3
e.g.:   [1,2,3] = [1-3]
        [-3, -1, 0, 1, 2, 3] = [-3, -1-3]
        [-3, -2, -1] = [-3--1]
"""

# first working solution
def solution(args):
    r = []
    stash = []
    for i in range(1, len(args)):
        if args[i] != args[i-1] + 1:
            if stash:
                r.append(stash)
                stash = []
            else:
                r.append([args[i-1]])
        else:
            if not stash: 
                stash.append(args[i-1])
            stash.append(args[i])
        if i == len(args)-1:
            if stash:
                r.append(stash)
            else:
                r.append([args[i]])
    res = []
    for l in r:
        if len(l) < 3:
            for i in l:
                res.append(str(i))
        else:
            res.append(f'{l[0]}-{l[-1]}')
    return ','.join(res)


# codewars solution
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)





a = solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) # returns "-6,-3-1,3-5,7-11,14,15,17-20"
print(a) 
