import json
from socket import *

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

destAddr = ('127.0.0.1', 8080)

send_data = {
    "CMD": "Init",
    "sFNTemplate": "c:/TMP/123.doc",
    "sFNSave": "c:/TMP/AAA.doc",
    "RSKey": "RS",
    "STSKey": "STS"
}
json_str = json.dumps(send_data)
buffer = repr(json_str)

udp_socket.sendto(buffer.encode('ascii'), destAddr)

udp_socket.close()
