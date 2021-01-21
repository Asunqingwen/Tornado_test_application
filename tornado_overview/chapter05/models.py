from peewee import *
db = MySQLDatabase('message', host="192.168.10.69", port=3306, user="root", password="root")

class Message(Model):
    id = AutoField(verbose_name="id")
    name = CharField(max_length=10, verbose_name="姓名")
    email = CharField(max_length=30, verbose_name="邮箱")  # index-建立索引
    address = CharField(max_length=30, verbose_name="地址")
    message = TextField(verbose_name="留言")

    class Meta:
        database = db
        table_name = "message"