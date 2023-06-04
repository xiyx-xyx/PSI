import random
import csv
import json
import requests
import time
class Do:
    def DO(self,b, n,prime, g, node):
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

        #print(node.id)
        #print(hash_table)
        #print(hash_table1)
        l = {}  # 存储正表秘密份额的
        l1 = {}  # 存储反表秘密份额的
        for i in range(n):
            l[i+1]=[]
            l1[i+1]=[]

        start = time.perf_counter()
        for secret in hash_table:
            shares = self.split_secret(secret, n)
            #print(shares)
            for i in shares:
                l[i[0]].append(i[1])


        for secret1 in hash_table1:
            shares1 = self.split_secret(secret1, n)
            #print(shares1)
            for i in shares1:
                l1[i[0]].append(i[1])
        end = time.perf_counter()
        print('用时：{:.5f}s'.format(end - start))

        '''print(l)
        print(l1)'''
        T1={}
        T2={}
        T1[node.id] = {}
        T1[node.id][1] = l[1]
        T1[node.id][0] = l1[1]

        T2[node.id] = {}
        T2[node.id][1] = l[2]
        T2[node.id][0] = l1[2]
        print(T1)
        print(T2)

        '''
        data = json.dumps(T1)
        url = "http://127.0.0.1:8000/server1"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)'''

        data1 = json.dumps(T1)
        url="http://111.132.6.120:8000/server1"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data1, headers=headers)
        print(x.content)


        data2 = json.dumps(T2)
        url="http://111.132.6.121:8000/server2"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data2, headers=headers)
        print(x.content)




    def split_secret(self,secret, n):
        shares = []
        if secret == 0:
            for x in range(1, n):
                share = random.randint(-200, 200)
                shares.append((x, share))
            shares.append((n, -sum([y for _, y in shares])))
        else:
            for x in range(1, n):
                share = random.randint(-200, 200)
                shares.append((x, share))
            shares.append((n, secret - sum([y for _, y in shares])))
        return shares

