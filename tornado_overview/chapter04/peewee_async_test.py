import asyncio

from chapter04.models.model import Goods
from chapter04.models.model import objects


async def handler():
    # await objects.create(Goods, supplier_id=7, name="飞天茅台", click_num=20, goods_num=1000, price=500, brief="贵州茅台")
    all_objects = await objects.execute(Goods.select())
    for obj in all_objects:
        print(obj.name)


loop = asyncio.get_event_loop()
loop.run_until_complete(handler())
# loop.close()
