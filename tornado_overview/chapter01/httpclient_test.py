from tornado import httpclient, ioloop
import asyncio


# http_client = httpclient.HTTPClient()
# try:
#     response = http_client.fetch("http://www.google.com/")
#     print(response.body)
# except httpclient.HTTPError as e:
#     # HTTPError is raised for non-200 responses; the response
#     # can be found in e.response.
#     print("Error: " + str(e))
# except Exception as e:
#     # Other errors are possible, such as IOError.
#     print("Error: " + str(e))
# http_client.close()

async def f():
    '''协程'''
    http_client = httpclient.AsyncHTTPClient()
    try:
        response = await http_client.fetch("https://www.tornadoweb.org/")
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body.decode("utf8"))


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    # 此方法可以在运行完某个协程后，停止事件循环
    io_loop.run_sync(f)

    # asyncio.ensure_future(f())
    # asyncio.get_event_loop().run_forever()

    
    # asyncio.get_event_loop().run_until_complete(f())
