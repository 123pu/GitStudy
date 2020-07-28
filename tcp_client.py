#   tcp客户端流程

import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server_addr = ('127.0.0.1',8585) #服务端地址
sockfd.connect(server_addr)

while True:
    # 发送消息
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("Server:",data.decode())

# 关闭套接字
sockfd.close()

