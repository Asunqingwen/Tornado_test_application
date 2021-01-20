# 1、什么是协程
# 1、回调过深，难以维护
# 2、栈撕裂造成异常无法向上抛出
# 3、协程——可以被暂定并切换到其他协程运行的函数

async def yield_test():
    yield 1
    yield 2
    yield 3
    return

async def main():
    await yield_test()

