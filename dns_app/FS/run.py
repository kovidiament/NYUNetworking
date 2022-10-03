from urllib import request
from flask import Flask
from flask import request
import time
import socket
app = Flask(__name__)




@app.route('/fibonacci', methods = ['GET'])
def hello_world():
    args = request.args.to_dict() 
    number = args.get("number")
    if number.isnumeric():
        n = int(number)
        if n == 0:
            return "0", 200
        a, b = 0, 1
        for i in range(0, n):
            a, b = b, a + b
        return str(a), 200
    return "not an int", 400



# curl -X PUT -H "Content-Type: application/json" -d "{\"hostname\":\"fibonacci.com\",\"ip\":\"0.0.0.0\", \"as_ip\":\"127.0.0.1\",\"as_port\":\"53533\"}" http://localhost:9090/register
@app.route('/register', methods = ['PUT'])
def fib():
    args = request.json
    host = args.get("hostname")
    ip = args.get("ip")
    as_ip = args.get("as_ip")
    as_port = args.get("as_port")
    registration_str = '''TYPE=A
    NAME={}
    VALUE={}
    TTL=10'''.format(host, ip)
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.sendto(registration_str.encode(), (as_ip, int(as_port)))
    client_sock.close()      
    return "registered", 201



app.run(host='0.0.0.0',
        port=9090,
        debug=True)