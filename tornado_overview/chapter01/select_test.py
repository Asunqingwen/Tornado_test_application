import socket

from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()


class Fetcher:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    host = "www.baidu.com"
    data = b""

    def get_url(self):
        try:
            self.client.connect((self.host, 80))  # 阻塞io，cpu处于空闲
        except BlockingIOError as _:
            pass

        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)  # 监听可写状态

    def connected(self, key):
        '''
        :param key: 文件描述符
        :return:
        '''
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format("/", self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)  # 监听可读状态

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode('utf8')
            print(data)


def loop_forever():
    # 时间循环
    while 1:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':
    fetcher = Fetcher()
    url = "http://www.baidu.com"
    fetcher.get_url()
    loop_forever()
