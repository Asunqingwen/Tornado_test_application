import asyncio
import aiomysql
from tornado import gen, ioloop


async def go():
    pool = await aiomysql.create_pool(host='192.168.10.69', port=3306,
                                      user='root', password='root',
                                      db='message', charset="utf8")
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * from message")
            value = await cur.fetchone()
            print(cur.description)
            print(value)
    pool.close()
    await pool.wait_closed()


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(go)
