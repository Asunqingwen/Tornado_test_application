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
        word = "aaaaa"
        # loader = web.template.Loader(
        #     "D:\\PythonProject\\Tornado_test_application\\tornado_overview\\chapter02\\templates")
        orders = [
            {
                "name": "小米T恤 忍者米兔双截棍 军绿 XXL",
                "image": "http://i1.mifile.cn/a1/T11lLgB5YT1RXrhCrK!40x40.jpg",
                "price": 39,
                "nums": 3,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            },
            {
                "name": "招财猫米兔 白色",
                "image": "http://i1.mifile.cn/a1/T14BLvBKJT1RXrhCrK!40x40.jpg",
                "price": 49,
                "nums": 2,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            },
            {
                "name": "小米圆领纯色T恤 男款 红色 XXL",
                "image": "http://i1.mifile.cn/a1/T1rrDgB4DT1RXrhCrK!40x40.jpg",
                "price": 59,
                "nums": 1,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            }
        ]
        self.render("index.html", orders=orders)
        # self.finish(loader.load("hello.html").generate(word=word))
        # self.render_string()


class MainHandler2(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，重载handler中不同的方法即可
    async def get(self, *args, **kwargs):
        '''重载get方法'''
        self.write("hello world2")


# 静态路径配置
settings = {
    "static_path": "D:\\PythonProject\\Tornado_test_application\\tornado_overview\\chapter02\\static",
    # "static_url_prefix": "/static/", #静态路径url前缀， 127.0.0.1:8888/static/
    "template_path": "templates",  # 模板路径配置
}

if __name__ == '__main__':
    # 声明APP
    # debug=true,修改自动生效
    app = web.Application([
        ("/", MainHandler),
        ("/2/?", RedirectHandler, {"url": "/"}),  # 永久重定向
        ("/static/(.*)", StaticFileHandler,
         {"path": "D:\\PythonProject\\Tornado_test_application\\tornado_overview\\chapter02\\static"}),  # 静态文件路径
    ], debug=False, **settings)
    # 监听端口
    app.listen(port=8888)
    ioloop.IOLoop.current().start()
