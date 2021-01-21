from chapter04.models.model import Supplier, Goods
from chapter04.data import supplier_list, goods_list


def save_model():
    # for data in supplier_list:
    #     supplier = Supplier()
    #     supplier.name = data["name"]
    #     supplier.address = data["address"]
    #     supplier.phone = data["phone"]
    #     supplier.save()
    for data in goods_list:
        good = Goods(**data)
        good.save()


def query_model():
    '''查询'''
    good = Goods.get(Goods.id == 1)
    # good = Goods.get_by_id(1)
    # good = Goods[1]

    # select * from goods
    goods = Goods.select(Goods.name, Goods.price).where(
        Goods.price > 100 and Goods.click_num > 300 and Goods.name.contains("茅台")).order_by(Goods.price.asc())
    # goods = Goods.select().order_by(Goods.price.asc())
    goods = Goods.select().order_by(Goods.price).paginate(2, 2)  # 分页，第几条开始，取几条数据
    for good in goods:
        print(good.price)


def update_model():
    try:
        good = Goods.get_by_id(1)
    except Goods.DoesNotExist:
        pass
    # good.click_num += 1
    # good.save()
    Goods.update(click_num=Goods.click_num + 1).where(Goods.id == 1).execute()
    good.delete_instance()
    Goods.delete().where(Goods.price > 150).execute()


if __name__ == '__main__':
    # save_model()
    # query_model()
    update_model()
