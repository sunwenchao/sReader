# a = 'aavsd'
# from string import maketrans
# b = maketrans('a', 'v')
# print a.translate(b)
# print a
# a = (1, 2)
# b = {}
# b[a] = '123';
# print b

import shelve

s = shelve.open('./data', 'c')
s['first'] = [12, 13]

s.close()

q = shelve.open('./data', 'r')
print q['first']

q.close()