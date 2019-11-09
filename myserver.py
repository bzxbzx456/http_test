from wsgiref.simple_server import make_server
from Application import application

# 创建服务器
server= make_server('127.0.0.1',9000,application)
print("server start at 9000")
# 开启事件循环，等待用户访问
server.serve_forever()
