import asyncio

@asyncio.coroutine
def hello():
    print('Hello World!')
    print('Start........')
    r = yield from asyncio.sleep(3)
    print('Done.........')
    print('Hello Again!!!!')

# 获取eventloop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()