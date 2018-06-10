from time import time
from timeit import default_timer as timer
# t = timer()
# '010101010101010000000000000000000000111111111111111111111111111111'[::-1]
# print(timer() - t)
# t = timer()
# str(reversed('010101010101010000000000000000000000111111111111111111111111111111'))
# print(timer() - t)

goog ={1:'0', 2:'001'}
def googol(n):
    if n in goog.keys():
        return goog[n]
    else:
        goog[n] = googol(n-1) + '0' + googol(n-1)[::-1].translate(str.maketrans('01', '10'))
        return goog[n]


