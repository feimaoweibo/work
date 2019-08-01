# 协程的终止 代码案例v03
def gen():
    for c in 'ABCDEF':
        yield c
# list 直接用生成器作为参数
print(list(gen()))
def gen_new():
    yield from 'HJKL'
print(list(gen_new()))