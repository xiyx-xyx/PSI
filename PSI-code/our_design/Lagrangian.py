import random
import json
import requests
class user:
    b = 7
    m = 3
    t = 2
    def receive_data_user(self,l, l1,):
        secret = []
        for i in range(self.b):
            shares = []
            shares1 = []
            c=0
            for key, value in l.items():
                if(c==self.t):
                    break
                share = (key, value[i])
                shares.append(share)
                c=c+1
            print(shares)
            x = self.combine_shares(shares)
            print(x)

            c=0
            for key, value in l1.items():
                if (c == self.t):
                    break
                share1 = (key, value[1])
                shares1.append(share1)
                c = c + 1
            print(shares1)

            x1 = self.combine_shares(shares1,self.t)
            print(x1)

            print("---------")
            if x / self.m == 1:
                if x1 == 0:
                    print("index {0} is intersection".format(i))
                    secret.append(i)
                else:
                    print("Send the arbitration request to the smart contract")
            else:
                print("index {0} is not intersection".format(i))

        print(secret)

    def combine_shares(self,shares,threshold):
        x_values, y_values = zip(*shares[:threshold])
        if len(set(x_values)) != len(x_values):
            raise ValueError("Shares are not distinct")
        secret = 0
        for i, y_i in enumerate(y_values):
            numerator, denominator = 1, 1
            for j, y_j in enumerate(y_values):
                if i == j:
                    continue
                numerator *= (0 - x_values[j])
                denominator *= (x_values[i] - x_values[j])
            secret += y_i * numerator // denominator
        return secret

if __name__ == '__main__':

    #send query to server
    qu='query'

    data = json.dumps(qu)
    url = "http:data user"
    headers = {
        "User-Agent": "123"
    }
    x = requests.post(url=url, data=data, headers=headers)
    print(x.content)

    url = "http:data user"
    headers = {
        "User-Agent": "123"
    }
    x = requests.post(url=url, data=data, headers=headers)
    print(x.content)

    url = "http:data user"
    headers = {
        "User-Agent": "123"
    }
    x = requests.post(url=url, data=data, headers=headers)
    print(x.content)

    #receive l and l1 from servers
    l = {1: [425, 366, 689, 554, 553, 483, 65], 2: [847, 729, 1251, 985, 1103, 827, 127],3: [1269, 1092, 1813, 1416, 1653, 1171, 189]}
    l1 = {1: [67, 605, 393, 526, 284, 669, 333], 2: [134, 1210, 786, 928, 568, 1168, 518],3: [201, 1815, 1179, 1330, 852, 1667, 703]}
    s=user()
    s.receive_data_user(l,l1)