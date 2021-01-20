from tornado.web import StaticFileHandler, RedirectHandler

# 1.RedirectHandler
# 1.301永久重定向，302临时重定向
import time

from tornado import web
from tornado import ioloop


class MainHandler(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，重载handler中不同的方法即可
    async def get(self, *args, **kwargs):
        '''重载get方法'''
        self.write("hello world")


class MainHandler2(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，重载handler中不同的方法即可
    async def get(self, *args, **kwargs):
        '''重载get方法'''
        self.write("hello world2")


# 静态路径配置
settings = {
    "static_path": "D:\\PythonProject\\Tornado_test_application\\tornado_overview\\chapter02\\static",
    # "static_url_prefix": "/static/", #静态路径url前缀， 127.0.0.1:8888/static/
}

if __name__ == '__main__':
    # 声明APP
    # debug=true,修改自动生效
    app = web.Application([
        ("/", MainHandler),
        ("/2/?", RedirectHandler, {"url": "/"}),  # 永久重定向
        ("/static3/(.*)", StaticFileHandler,
         {"path": "D:\\PythonProject\\Tornado_test_application\\tornado_overview\\chapter02\\static"}),  # 静态文件路径
    ], debug=True, **settings)
    # 监听端口
    app.listen(port=8888)
    ioloop.IOLoop.current().start()
