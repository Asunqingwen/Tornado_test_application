import time

from tornado import web
from tornado import ioloop


class MainHandler(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，重载handler中不同的方法即可
    async def get(self, *args, **kwargs):
        '''重载get方法'''
        time.sleep(5)
        self.write("hello world")

class MainHandler2(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，重载handler中不同的方法即可
    async def get(self, *args, **kwargs):
        '''重载get方法'''
        self.write("hello world2")

if __name__ == '__main__':
    # 声明APP
    # debug=true,修改自动生效
    app = web.Application([
        ("/", MainHandler),
        ("/2/", MainHandler2),
    ], debug=True)
    # 监听端口
    app.listen(port=8888)
    ioloop.IOLoop.current().start()
