def application(environ,start_response):
    # 第一个参数是状态码
    # 第二个参数是一个列表 列表的每一个元素是一个二元祖（key,value）
    path = environ['PATH_INFO']
    start_response("200 ok",[("Content-Type",'text/html'),('hello','close')])
    if path == "/":
        return [b'hello world']
    return [b'not found']