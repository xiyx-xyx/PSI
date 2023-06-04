import random
import json
import requests
import threading
import datetime
import requests
class user:
    b = 100
    m = 3
    t = 2

    def receive_data_user(self, shares ):
        secret=[]
        for i in range(self.b):
            T=[]
            T1=[]
            for key1, value1 in shares.items():
                print("from server:{0}".format(key1))
                for key2, value2 in value1.items():
                    if key2 == '1':
                        share = (int(key1), value2[i])
                        T.append(share)
                    if key2 == '0':
                        share1 = (int(key1), value2[i])
                        T1.append(share1)
            print(T)
            print(T1)
            x=self.combine_shares(T,self.t)
            x1=self.combine_shares(T1,self.t)
            print(x)
            print(x1)
            print("-----------")
            if x / self.m == 1:
                if x1 == 0:
                    print("index {0} is intersection".format(i))
                    secret.append(i)
                else:
                    print("Send the arbitration request to the smart contract")
            else:
                print("index {0} is not intersection".format(i))

        print(secret)

    def combine_shares(self, shares, threshold):
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
    # send query to server

    data = 'query'

    def send_request(url):
        # 获取当前时间
        now = datetime.datetime.now()

        # 格式化为字符串
        time_str = now.strftime("%H:%M:%S.%f")[:-3]

        # 输出当前时间
        print("当前时间为：", time_str)
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)


    urls = [
        "http://111.132.6.120:8000/user1",
        "http://111.132.6.121:8000/user2",
    ]

    threads = []

    for url in urls:
        t = threading.Thread(target=send_request, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    '''Judgment = {}

    Judgment['owner'] = ['owner1','owner2','owner3']
    Judgment['server'] = [{'name':'server1','url':'http://111.132.6.120:8000/smartcontract1'},{'name':'server2','url':'http://111.132.6.121:8000/smartcontract2'}]
    Judgment["eventid"] = 'e002'
    print(Judgment)
    data = json.dumps(Judgment)
    url = "http://111.132.6.51:2001/www/psi/trans/judge"
    headers = {
        "User-Agent": "123"
    }
    x = requests.post(url=url, data=data, headers=headers)
    print(x.content)'''
