# 权重
'''
goods = [{"name":"good1", "price":200, "sales":100, "stars":5, "comments":400},
         {"name":"good2", "price":300, "sales":120, "stars":4, "comments":500},
         {"name":"good3", "price":500, "sales":3000, "stars":2, "comments":199},
         {"name":"good4", "price":1288, "sales":8, "stars":5, "comments":398},
         {"name":"good5", "price":899, "sales":99, "stars":5, "comments":2000}]
- 权重是100
- 价格占的权重是40%,销量占的权重是17%,评级占的权重是13%,评论占的权重是30%
'''

# 使用sorted()函数排序,权重按默认升序排列
goods = [{"name":"good1", "price":200, "sales":100, "stars":5, "comments":400},
         {"name":"good2", "price":300, "sales":120, "stars":4, "comments":500},
         {"name":"good3", "price":500, "sales":3000, "stars":2, "comments":199},
         {"name":"good4", "price":1288, "sales":8, "stars":5, "comments":398},
         {"name":"good5", "price":899, "sales":99, "stars":5, "comments":2000}]
def diySorted(args):
    price = args['price']
    sales = args['sales']
    stars = args['stars']
    comment = args['comments']
    data = price*0.4 + sales*0.17 + stars*0.13 + comment*0.3
    return data
diy1 = sorted(goods,key=diySorted)
print(diy1)

# 使用匿名函数 lambda() 表达式，权重进行降序排列
diy2 = sorted(goods, key=lambda x: x['price']*0.4 +x['sales']*0.17 +x['stars']*0.13 +x['comments']*0.3, reverse=True)
print(diy2)