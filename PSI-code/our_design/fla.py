from flask import Flask, request, jsonify
import json
import time
from storage_server import *
import csv

app = Flask(__name__)

shares = {}
count = 0

def combine(data):
    global count
    global shares
    count += 1
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    shares.update(data_dict)
    #print(shares)
    if count == 3:
        '''with open('shares.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for key, value in shares.items():
                for sub_key, sub_value in value.items():
                    row = [key, sub_key] + sub_value
                    writer.writerow(row)'''
        t = server()
        #start = time.perf_counter()
        t.receive_data_server(shares)
        #end = time.perf_counter()
        #print('用时：{:.5f}s'.format(end - start))

@app.route('/server1', methods=['POST'])
def server1():
    data = request.get_data()
    combine(data)
    return 'ok'

@app.route('/smartcontract1', methods=['POST'])
def smartcontract1():
    data = request.get_data()
    e = int(data)
    print(data)
    t = server()
    return t.proof(e)

@app.route('/user1', methods=['POST'])
def user():
    data = request.get_data().decode('utf-8')
    print(data)
    if data == 'query':
        print("--------")
        shares_read = {}
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
        t.receive_data_server(shares_read)
        return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)


'''from flask import Flask, request, jsonify
import json
import time
from storage_server import *


class ServerApp:
    def __init__(self, host='0.0.0.0', port=8000, debug=True):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.debug = debug
        self.shares = {}
        self.count = 0
        self.init_routes()

    def init_routes(self):
        self.app.route('/server1', methods=['POST'])(self.server1)

    def server1(self):
        data = request.get_data()
        self.combine(data)
        return 'ok'

    def combine(self, data):
        self.count += 1
        data_str = data.decode('utf-8')
        data_dict = json.loads(data_str)
        self.shares.update(data_dict)
        print(self.shares)
        if self.count == 3:
            t = server()
            start = time.perf_counter()
            t.receive_data_server(self.shares)
            end = time.perf_counter()
            print('用时：{:.5f}s'.format(end - start))

    def run(self):
        self.app.run(debug=self.debug, host=self.host, port=self.port)
if __name__ == '__main__':
    server_app = ServerApp()
    server_app.run()
'''
