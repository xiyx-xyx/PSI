from Lagrangian import *
import csv
import json
import requests
import time
from secrets import randbelow
from multiprocessing import Process
from node import *
import sys
class Do:
    def init(self,b, n, t, p, g, m):
        processList = []
        nodeList = []
        for i in range(m):
            nodeList.append(Node(i+1))
            owner = Process(target=self.DO, args=(b, n, t, p, g, nodeList[i]))
            processList.append(owner)
        return processList

    def DO(self,b, n, t, prime, g, node):
        print('Start Owner {0}.'.format(node.id))
        hash_table = [None] * b
        hash_table1 = [None] * b
        for i in range(0, b):
            random_value = random.randint(2, 100)
            hash_table[i] = random_value
            random_value = random.randint(2, 100)
            hash_table1[i] = random_value

        # Define the hash function
        def hash_function(data, size):
            hash_value = hash(data) % size
            return hash_value
        # Read data from file
        if (node.id==1):
            with open('psi_1.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), b)
                    # print(index)
                    hash_table[index] = 1
                    hash_table1[index] = 0
        elif(node.id==2):
            with open('psi_2.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), b)
                    # print(index)
                    hash_table[index] = 1
                    hash_table1[index] = 0
        elif(node.id==3):
            with open('psi_3.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), b)
                    # print(index)
                    hash_table[index] = 1
                    hash_table1[index] = 0
        elif (node.id == 4):
            with open('psi_4.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), b)
                    # print(index)
                    hash_table[index] = 1
                    hash_table1[index] = 0
        #print(node.id)
        #print(hash_table)
        #print(hash_table1)
        '''shuffled_list = [hash_table1[i] for i in (permutation_list)]
        print(shuffled_list)'''

        l = {}  # 存储正表秘密份额的
        l1 = {}  # 存储反表秘密份额的
        d = {}  # 存储发送给智能合约的摘要
        for i in range(n):
            l[i+1]=[]
            l1[i+1]=[]
            d["server"+str(i + 1)]=[]

        start = time.perf_counter()
        for secret in hash_table:
            shares = self.generate_shares(secret, n, t)
            #print(shares)
            for i in shares:
                l[i[0]].append(i[1])
                d["server"+str(i[0])].append(pow(g, i[1], prime))


        for secret1 in hash_table1:
            shares1 = self.generate_shares(secret1, n, t)
            #print(shares1)
            for i in shares1:
                l1[i[0]].append(i[1])
        end = time.perf_counter()
        print('用时：{:.5f}s'.format(end - start))

        #print(l)
        #print(l1)
        #print(d)
        dd={}
        dd["owner" + str(node.id)]=d
        dd["eventid"] = "e002"
        #print(dd)

        '''data = json.dumps(dd)
        url = "http://111.132.6.51:2001/www/psi/trans/dataowner"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)'''

        T1={}
        T2={}
        T3={}
        T4={}
        T1[node.id] = {}
        T1[node.id][1] = l[1]
        T1[node.id][0] = l1[1]

        T2[node.id] = {}
        T2[node.id][1] = l[2]
        T2[node.id][0] = l1[2]

        T3[node.id] = {}
        T3[node.id][1] = l[3]
        T3[node.id][0] = l1[3]

        '''T4[node.id] = {}
        T4[node.id][1] = l[4]
        T4[node.id][0] = l1[4]
        print(T1)
        print(T2)
        print(T3)
        print(T4)'''

        data1 = json.dumps(T1)
        url="http://111.132.6.120:8000/server1"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data1, headers=headers)
        print(x.content)


        data2 = json.dumps(T2)
        url="http://111.132.6.121:8100/server2"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data2, headers=headers)
        print(x.content)

        data3 = json.dumps(T3)
        url="http://111.132.6.123:8000/server3"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data3, headers=headers)

        '''data4 = json.dumps(T4)
        url = "http://111.132.6.123:8000/server4"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data4, headers=headers)'''


    def generate_shares(self,secret, num_shares, threshold):
        if threshold > num_shares:
            raise ValueError("Threshold cannot be greater than the number of shares")
        if secret < 0:
            raise ValueError("Secret cannot be negative")
        shares = []
        coefficients = [secret] + [randbelow(256) for _ in range(threshold - 1)]
        # print(coefficients)
        for i in range(1, num_shares + 1):
            share = coefficients[0]
            for j in range(1, threshold):
                share += coefficients[j] * (i ** j)
            shares.append((i, share))
        return shares
