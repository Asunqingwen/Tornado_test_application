# define options

import time

from tornado import web
from tornado import ioloop
from tornado.options import define, options, parse_command_line

# define 定义一些可以在命令行中传递的参数以及类型
define('port', default=8008, help="run on the given port", type=int)
define('debug', default=False, help="set tornado debug mode", type=int)

# options是一个类，全局只有一个options
# 命令行
# options.parse_command_line()
# 配置文件
options.parse_config_file("conf.cfg")


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


if __name__ == '__main__':
    # 声明APP
    # debug=true,修改自动生效
    app = web.Application([
        ("/", MainHandler),
        ("/2/", MainHandler2),
    ], debug=True)
    # 监听端口
    app.listen(port=options.port)
    ioloop.IOLoop.current().start()
