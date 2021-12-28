# first working solution
def order(sentence):
    order_dc = {}
    for word in sentence.split(' '):
        digit = ''.join(filter(lambda i: i.isdigit(), word)) 
        order_dc[digit] = word
    return ' '.join([order_dc[k] for k in sorted(list(order_dc.keys()))])

# shorter version (not working yet)
# def order(sentence):
#     digits = [int(''.join(filter(lambda i: i.isdigit(), w))) for w in sentence.split(' ')]
#     print(digits)
#     for d in digits:
#         print(sentence.split(' ')[d-1])
#     return ' '.join([sentence.split(' ')[d-1] for d in digits])




print(order("is2 Thi1s T4est 3a")) # "Thi1s is2 3a T4est"
print(order('g3ood 4of the2 pe6ople th5e Fo1r'))
print(order(''))