from tornado.web import StaticFileHandler, RedirectHandler
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
        id = ""
        name = ""
        email = ""
        address = ""
        message = ""
        pool = await aiomysql.create_pool(host=self.db['host'], port=self.db['port'],
                                          user=self.db['user'], password=self.db['password'],
                                          db=self.db['name'], charset=self.db['charset'])
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT id,name,email,address,message from message")
                id, name, email, address, message = await cur.fetchone()
        pool.close()
        await pool.wait_closed()

        self.render("message.html", id=id, name=name, email=email, address=address, message=message)

    async def post(self, *args, **kwargs):
        '''重载post方法'''
        id = self.get_body_argument("id", "")
        name = self.get_body_argument("name", "")
        email = self.get_body_argument("email", "")
        address = self.get_body_argument("address", "")
        message = self.get_body_argument("message", "")
        pool = await aiomysql.create_pool(host=self.db['host'], port=self.db['port'],
                                          user=self.db['user'], password=self.db['password'],
                                          db=self.db['name'], charset=self.db['charset'])
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                if not id:
                    await cur.execute(
                        "insert into message(name,email,address,message) values ('{}','{}','{}','{}')".format(name,
                                                                                                              email,
                                                                                                              address,
                                                                                                              message))
                else:
                    await cur.execute(
                        "update message set name='{}',email='{}',address='{}',message='{}'".format(name, email, address,
                                                                                                   message))
                await conn.commit()
        pool.close()
        await pool.wait_closed()
        self.render("message.html", id=id, name=name, email=email, address=address, message=message)


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
