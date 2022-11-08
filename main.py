import hashlib
# N = int(input())
# num = input()
N = 2
num = '1 2'
the_tuple = tuple(num.split(' ',N))
print(hash(the_tuple))
