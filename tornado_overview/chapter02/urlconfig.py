from tornado import web
from tornado import ioloop
import tornado


class MainHandler(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，重载handler中不同的方法即可
    async def get(self, *args, **kwargs):
        '''重载get方法'''
        self.write("hello world")


class PeopleIdHandler(web.RequestHandler):
    def initialize(self, name):
        self.db_name = name

    @tornado.web.addslash
    async def get(self, id, *args, **kwargs):
        self.redirect(self.reverse_url("people_name", self.db_name))


class PeopleNameHandler(web.RequestHandler):
    @tornado.web.addslash
    async def get(self, name, *args, **kwargs):
        self.write("用户姓名:{}".format(name))


class PeopleInfoHandler(web.RequestHandler):
    @tornado.web.addslash
    async def get(self, name, age, gender, *args, **kwargs):
        self.write("用户姓名:{},用户年龄:{},用户性别:{}".format(name, age, gender))


people_db = {
    "name": "people",
}

urls = [
    tornado.web.URLSpec("/", MainHandler, name="index"),
    tornado.web.URLSpec("/people/(\d+)/?", PeopleIdHandler, people_db, name="people_id"),  # 配置如/people/1/
    tornado.web.URLSpec("/people/(\w+)/?", PeopleNameHandler, name="people_name"),  # 配置如/people/name/
    tornado.web.URLSpec("/people/(?P<name>\w+)/(?P<age>\d+)/(?P<gender>\w+)/?", PeopleInfoHandler, name="people_info"),
    # 配置如/people/name/age/gender/
]

if __name__ == '__main__':
    # 声明APP
    # debug=true,修改自动生效
    app = web.Application(urls, debug=False)
    # 监听端口
    app.listen(port=8888)
    ioloop.IOLoop.current().start()

# 1、url各种参数配置
# 2、url命名reverse_url
# 3、handler传入初始值
