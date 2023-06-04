from flask import Flask, request
import json
import time
from datauser import *
import datetime

class Myuser:
    def __init__(self):
        self.app = Flask(__name__)
        self.shares = {}
        self.count = 0
        self.app.route('/datauser', methods=['POST'])(self.datauser)

    def start(self):
        self.app.run(debug=True, host="0.0.0.0", port=8000)

    def datauser(self):
        data = request.get_data()
        self.combine(data)
        return 'ok'

    def combine(self, data):
        global shares
        self.count += 1
        data_str = data.decode('utf-8')
        data_dict = json.loads(data_str)
        self.shares.update(data_dict)
        print(self.shares)
        if self.count == 2:
            # 获取当前时间
            now = datetime.datetime.now()
            # 格式化为字符串
            time_str = now.strftime("%H:%M:%S.%f")[:-3]
            # 输出当前时间
            print("当前时间为：", time_str)

            t = user()
            start = time.perf_counter()
            t.receive_data_user(self.shares)
            end = time.perf_counter()
            print('插值和验证用时：{:.5f}s'.format(end - start))

if __name__ == '__main__':
    s = Myuser()
    s.start()
