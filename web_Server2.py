import socket
from threading import Thread

def main():
    #1.建立socket
    server = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    #复用socket
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 2.给服务器绑定地址
    server.bind(('',8000))

    # 把服务器变被动监听
    server.listen(5)
    print("server start at 8000")
    try:
        while True:
            # 接收客户端链接
            # client 客户端的socket  clientAddr 客户端的地址
            clientSocket,clientAddr = server.accept()
            print(clientSocket,clientAddr)

            # 启动一个新线程处理客户端请求
            # application 处理客户端请求 可能是一个函数或者可能是一个类
            client = Thread(target=application,args=(clientSocket,clientAddr))
            client.start()
    except Exception as e:
        print(e)
    finally:
        server.close()

def application(clientSocket,clientAddr):
    """
    处理客户端的请求
    :param clientSocket: 客户端socket
    :param clientADdr: 客户端地址
    :return: 返回一个html源码
    """
    print(clientSocket,clientAddr)
    request = clientSocket.recv(1024)
    # 把请求消息分割成列表
    req = request.decode('utf-8').splitlines()
    #取出请求行（第一行）获取请求路径
    req = req[0].split(" ")[1]
    print(req)
    if req == "/":
        html = "HTTP/1.1 200 ok\r\nConnection: close\r\n\r\n"
        html += "<h1>Hello World</h1>"
    elif req == "/hello":
        html = "HTTP/1.1 200 ok\r\nConnection: close\r\n\r\n"
        html += "<h1>World</h1>"
    elif req == "/world":
        html = "HTTP/1.1 200 ok\r\nConnection: close\r\n\r\n"
        html += "<h1>Hello</h1>"
    else:
        html = "HTTP/1.1 200 ok\r\nConnection: close\r\n\r\n"
        html += "<h1>Page Not Found</h1>"
    clientSocket.send(html.encode('utf-8'))
    clientSocket.close()

if __name__ == '__main__':
    main()