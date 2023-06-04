import random
from Crypto.Util import number
from sympy import primefactors
from dataowner import *
from node import *
def main():
    # Initialize the hash table
    print("system setup")
    b = 1600
    n = 2
    m = 3

    #p = number.getPrime(9)
    #q = max(primefactors(p - 1))
    #g = number.getRandomRange(2, p - 1)
    p=443
    q=17
    g=87
    print("p:{0}".format(p))
    print("q:{0}".format(q))
    print("g:{0}".format(g))
    #permutation_list = random.sample(range(b), b)
    #print(permutation_list)

    s=Do()
    for i in range(m):
        node = Node(i+1)
        s.DO(b, n, p, g, node)



# start = time.perf_counter()  # 返回系统运行时间
# end = time.perf_counter()
# print('用时：{:.5f}s'.format(end - start))

if __name__ == '__main__':
    main()
