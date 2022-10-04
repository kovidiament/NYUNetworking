import urllib
from flask import Flask
from flask import request
import time
import socket

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/fibonacci', methods = ['GET'])
def fib():
    args = request.args.to_dict() 
    host = args.get("hostname")
    fs_port = args.get("fs_port")
    number = args.get("number")
    as_ip = args.get("as_ip")
    as_port = args.get("as_port")
    if host is None or fs_port is None or number is None or as_ip is None or as_port is None:
        return "Bad request", 400
    query = '''TYPE=A
    NAME={}'''.format(host).encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(query, (as_ip, int(as_port)))
    fib_ip = sock.recvfrom(2048)[0].decode().split('\n')[2].split("=")[1]
    print("fib IP = ",fib_ip)
    query_addr = 'http://'+fib_ip+':'+fs_port+'/fibonacci?number='+number
    
    with urllib.request.urlopen(query_addr) as response:
        answer = response.read()
       

            
    return str(int(answer)), 200

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
