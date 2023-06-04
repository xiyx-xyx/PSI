import random
import json
import requests
import threading
import datetime
import requests
class user:
    p = 11
    q = 143
    t = 5
    g = 3
    b = 100

    def receive_data_user(self, shares):
        secret=[]
        for i in range(self.b):
            s=1
            s1=1
            for key1, value1 in shares.items():
                print("from server:{0}".format(key1))
                for key2, value2 in value1.items():
                    if key2 == '1':
                        s=value2[i]*s
                    if key2 == '0':
                        s1=value2[i]*s1
            print(s%self.p)
            print(s1%self.p)
            if s%self.p== 1:
                if s1%self.p == 1:
                    print("index {0} is intersection".format(i))
                    secret.append(i)
                else:
                    print("Send the arbitration request to the smart contract")
            else:
                print("index {0} is not intersection".format(i))

        print(secret)

if __name__ == '__main__':
    # send query to server

    data = 'query'

    def send_request(url):
        # 获取当前时间
        now = datetime.datetime.now()

        # 格式化为字符串
        time_str = now.strftime("%H:%M:%S.%f")[:-3]

        # 输出当前时间
        print("当前时间为send：", time_str)

        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)


    urls = [
        "http://111.132.6.120:8000/user1",
        "http://111.132.6.121:8000/user1"
    ]

    threads = []

    for url in urls:
        t = threading.Thread(target=send_request, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    '''share={'1': {'1': [27, 27, 81], '0': [27, 81, 3]},'2': {'1': [9, 1, 1], '0': [9, 27, 1]}}
    s=user()
    s.receive_data_user(share)'''
