from tornado.web import RequestHandler
from tornado import web, ioloop
import tornado


class MainHandler(RequestHandler):
    # 入口
    # def initialize(self, db):
    #     # 用于初始化handler类的过程
    #     self.db = db

    def prepare(self):
        # prepare方法用于真正调用请求处理之前的初始化方法
        # 1、打印日志，打开文件
        pass

    def on_finish(self) -> None:
        # 关闭句柄，清理内存
        pass

    # http方法
    @tornado.web.addslash
    def get(self, *args, **kwargs):
        # data1 = self.get_query_argument()
        # data2 = self.get_query_arguments()
        data1 = self.get_argument('name')
        data2 = self.get_arguments('name')
        pass

    def post(self, *args, **kwargs):
        data1 = self.get_argument()
        data2 = self.get_arguments()
        pass

    def delete(self, *args, **kwargs):
        pass

    # 输出
    # 1.set_status,write_error,finish,redirect,write
    def write_error(self, status_code: int, **kwargs) -> None:
        pass


urls = [
    web.URLSpec("/", MainHandler, name="index"),
]

if __name__ == '__main__':
    # 声明APP
    # debug=true,修改自动生效
    app = web.Application(urls, debug=True)
    # 监听端口
    app.listen(8888)
    ioloop.IOLoop.current().start()
