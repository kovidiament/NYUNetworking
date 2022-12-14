from fileinput import filename
import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 53533))

records = {}


while True:
    msg, addr = sock.recvfrom(2048)
    message = msg.decode()
    query = message.split('\n')
    print('query received at AS is\n',query)
    if len(query) > 2:
        name = query[1].split('=')[1]
        value = query[2].split('=')[1]
        records[name] = value
        print('setting records[',name,'] to be ', value)
    else:
        name = query[1].split('=')[1]
        value = records[name]
        response = '''TYPE=A
        NAME={}
        VALUE={}
        TTL=10'''.format(name, value)
        sock.sendto(response.encode(), addr)
        print("response is ", response)
