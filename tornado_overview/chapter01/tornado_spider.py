from urllib.parse import urljoin

from bs4 import BeautifulSoup
from tornado import gen, httpclient, ioloop, queues

base_url = "https://www.tornadoweb.org/en/stable/"
concurrency = 3


async def get_url_links(url):
    response = await httpclient.AsyncHTTPClient().fetch(url)
    html = response.body.decode("utf8")
    soup = BeautifulSoup(html,features="html.parser")
    links = [urljoin(base_url, a.get("href")) for a in soup.find_all("a", href=True)]
    return links


async def main():
    q = queues.Queue()  # 非阻塞队列
    visited = set()

    async def fetch_url(current_url):
        '''生产者'''
        if current_url in visited:
            return
        print("获取：{}".format(current_url))
        visited.add(current_url)
        next_url = await get_url_links(current_url)
        for new_url in next_url:
            if new_url.startswith(base_url):
                await q.put(new_url)

    async def worker():
        '''消费者'''
        async for url in q:
            if url is None:
                return
            try:
                await fetch_url(url)
            except Exception as e:
                print("exception:" % e)
            finally:
                q.task_done()

    # 放入初始url
    await q.put(base_url)

    # 启动协程
    workers = gen.multi([worker() for _ in range(concurrency)])  # 初始化多个协程
    await q.join()

    for _ in range(concurrency):
        await q.put(None)

    await workers


if __name__ == '__main__':
    # base_url = "http://baidu.com"
    # next_url = "/bobby/"
    # print(urljoin(base_url,next_url))
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
