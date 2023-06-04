import random
from Crypto.Util import number
from sympy import primefactors
from dataowner import *
def run(processList):
    for process in processList:
        process.start()
    for process in processList:
        process.join()

def main():
    # Initialize the hash table
    #send those to server/smart contract
    print("system setup")
    b = 800
    n = 3
    m = 3
    t = 2
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
    '''processList = s.init(b,n,t,p,g,m)
    run(processList)'''
    for i in range(m):
        node = Node(i+1)
        s.DO(b, n, t, p, g, node)



# start = time.perf_counter()  # 返回系统运行时间
# end = time.perf_counter()
# print('用时：{:.5f}s'.format(end - start))

if __name__ == '__main__':
    main()