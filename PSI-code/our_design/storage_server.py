from Crypto.Util import number
import requests
import json
import time
import fla
import sys
import csv
class server:
    id=1
    p=443
    q=17
    g=87
    b =100
    r = 13

    def generate_keypair(self):
        # Compute the public key y = g^x mod p
        print(self.r)
        o = pow(self.g, self.r, self.p)
        return o

    def receive_data_server(self, shares):

        res = {}
        res[self.id] = {}
        l = []
        l1 = []
        for i in range(self.b):
            s = 0
            s1 = 0
            for key1, value1 in shares.items():
                #print("from data owner:{0}".format(key1))
                for key2, value2 in value1.items():
                    if key2 == '1':
                        s = s + value2[i]
                    if key2 == '0':
                        s1 = s1 + value2[i]
            l.append(s)
            l1.append(s1)
        res[self.id][1] = l
        res[self.id][0] = l1
        with open('l.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(l)

        print(l)
        #print(l1)
        #print(res)

        data = json.dumps(res)
        url = "http://111.132.6.122:8000/datauser"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)


    def proof(self, e):
        z=[]
        z_sc={}
        l_read = []
        with open('l.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                l_read = list(map(int, row))
        print(l_read)

        #start = time.perf_counter()
        for i in l_read:
            z.append((self.r + e * i) % self.q)
        #end = time.perf_counter()
        #print('用时：{:.5f}s'.format(end - start))
        #z_sc["server"+str(self.id)]=z
        #byte_size = sys.getsizeof(z)
        #print(byte_size*16)
        data = json.dumps(z)
        str_list = [str(num) for num in z]  # 将列表中的每个元素转换为字符串
        str_result = ','.join(str_list)  # 使用逗号作为分隔符连接字符串列表
        print(str_result)  # 输出：'1,2,3'
        return str_result
        '''url = "http:data /ar_proof"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)'''

if __name__ == '__main__':
    # receive l and l1 from data owner
    #shares = {'1': {'1': [1, 2, 3], '0': [1, 2, 4]}, '2': {'1': [3, 4, 5], '0': [5, 6, 7]}}
    '''shares_read = {}
    with open('shares.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            key = row[0]
            sub_key = row[1]
            sub_value = row[2:]
            if key not in shares_read:
                shares_read[key] = {}
            shares_read[key][sub_key] = list(map(int, sub_value))
    print(shares_read)
    t = server()
    t.receive_data_server(shares_read)'''

    s = server()
    # send o to smart contract
    o_sc = {}
    o=s.generate_keypair()
    o_sc["server"+str(s.id)] = o
    o_sc["eventid"]='e001'
    print(o_sc)
    data = json.dumps(o_sc)
    url = "http://111.132.6.51:2001/api/psi/trans/server"
    headers = {
        "User-Agent": "123"
    }
    x = requests.post(url=url, data=data, headers=headers)
    print(x.content)

