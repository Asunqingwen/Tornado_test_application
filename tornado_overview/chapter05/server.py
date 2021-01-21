from tornado.web import StaticFileHandler, RedirectHandler
from chapter05.forms import MessageForm
from chapter05.models import Message
# 1.RedirectHandler
# 1.301永久重定向，302临时重定向
import time

from tornado import web
from tornado import ioloop
import aiomysql


class MainHandler(web.RequestHandler):
    def initialize(self, db) -> None:
        self.db = db

    # 当客户端发起不同的http方法的时候，重载handler中不同的方法即可
    async def get(self, *args, **kwargs):
        '''重载get方法'''
        message_form = MessageForm()

        self.render("message.html", message_form=message_form)

    async def post(self, *args, **kwargs):
        '''重载post方法'''
        message_form = MessageForm(self.request.arguments)
        if message_form.validate():
            # 验证通过
            name = message_form.name.data
            email = message_form.email.data
            address = message_form.address.data
            message_data = message_form.message.data

            message = Message()
            message.name = name
            message.email = email
            message.address = address
            message.message = message_data

            message.save()
            self.render("message.html", message_form=message_form)
        else:
            self.render("message.html", message_form=message_form)


# 静态路径配置
settings = {
    "static_path": "D:\\PythonProject\\Tornado_test_application\\tornado_overview\\chapter03\\static",
    "static_url_prefix": "/static/",  # 静态路径url前缀， 127.0.0.1:8888/static/
    "template_path": "templates",  # 模板路径配置
    # 数据库配置
    "db": {
        "host": "192.168.10.69",
        "user": "root",
        "password": "root",
        "name": "message",
        "port": 3306,
        "charset": "utf8",
    }
}

# url配置
urls = [
    ("/", MainHandler, {"db": settings["db"]}),
    ("/static/(.*)", StaticFileHandler,
     {"path": "D:\\PythonProject\\Tornado_test_application\\tornado_overview\\chapter03\\static"}),  # 静态文件路径
]

if __name__ == '__main__':
    # 声明APP
    # debug=true,修改自动生效
    app = web.Application(urls, autoreload=False, **settings)
    # 监听端口
    app.listen(port=8888)
    ioloop.IOLoop.current().start()
