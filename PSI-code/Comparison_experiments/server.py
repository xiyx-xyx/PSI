from Crypto.Util import number
import requests
import json
import time
import fla
import sys
import csv
class server:
    id=1

    p=11
    q=143
    t=5
    g=3
    b =100

    def receive_data_server(self, shares):
        res = {}
        res[self.id] = {}
        l = []
        l1 = []
        for i in range(self.b):
            s = 0
            s1 = 0
            for key1, value1 in shares.items():
                for key2, value2 in value1.items():
                    if key2 == '1':
                        s = s + value2[i]
                    if key2 == '0':
                        s1 = s1 + value2[i]
            s_end=pow(self.g,((s%self.t)-1)%self.t,self.q)
            s1_end=pow(self.g,s1%self.t,self.q)
            l.append(s_end)
            l1.append(s1_end)

        res[self.id][1] = l
        res[self.id][0] = l1

        print(l)
        print(l1)
        print(res)

        '''data = json.dumps(res)
        url = "http://127.0.0.1:8000/datauser"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)'''



if __name__ == '__main__':
    # receive l and l1 from data owner
    '''shares = {'1': {'1': [4, 2, 3], '0': [2, 0, 1]}, '2': {'1': [3, 4, 3], '0': [2, 3, 4]},'3': {'1': [2, 3, 4], '0': [4, 1, 1]}}
    t = server()
    t.receive_data_server(shares)'''
