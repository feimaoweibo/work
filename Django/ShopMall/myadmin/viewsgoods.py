from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Types, Goods
from PIL import Image
import time, os, json

# 浏览商品类别信息
def typeindex(request):
    '''
    执行数据查询，并放置到模版中
    :param request: concat负责把path和id拼接成一个内容。
           说明文档查询：https://docs.djangoproject.com/en/1.11/ref/models/querysets/#extra
    :return: 如果是mysql版本，需要时hi用concat，如果是sqlite，则需要使用 || 链接path和id
             list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    '''
    list = Types.objects.extra(select={'_has': 'path || id'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    for ob in list:
        ob.pname = '...'*(ob.path.count(',')-1)
        # print(list[0].__dict__)
    context = {"typeslist": list}
    return render(request, "myadmin/type/index.html", context)
# 商品类别信息添加表单
def typeadd(request,tid):
    # 获取父类别信息，若没有则默认为根类别信息
    if tid == '0':
        context = {'pid': 0, 'path': '0,', 'name': '根类别'}
    else:
        ob = Types.objects.get(id=tid)
        context = {'pid': ob.id, 'path': ob.path+str(ob.id)+',', 'name': ob.name}
    return render(request, "myadmin/type/add.html", context)

# 执行商品类别信息添加
def typeinsert(request):
    try:
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        ob.path = request.POST['path']
        ob.save()
        context = {'info': "添加成功！"}
    except:
        context = {'info': "添加失败！！！"}
    return render(request, "myadmin/info.html", context)

# 商品类别信息删除表单
def typedel(request,tid):
    try:
        # 获取删除商品的子列表信息里，诺有数据，就禁止删除当前类别
        row = Types.objects.filter(pid=tid).count()
        if row > 0:
            context = {'info':'禁止删除：此类别下还有子类'}
            return render(request, "myadmin/info.html", context)
        ob = Types.objects.get(id=tid)
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info': '删除失败'}
    return render(request, "myadmin/info.html", context)

# 商品类型信息编辑表单
def typeedit(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        context = {'type': ob}
        return render(request, "myadmin/type/edit.html", context)
    except:
        context = {'info': '没有找到要修改的信息'}
    return render(request, "myadmin/info.html", context)

# 商品类型添加表单
def typeupdate(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        ob.name = request.POST['name']
        ob.save()
        context = {'info': '修改成功'}
    except:
        context = {'info': '修改失败'}
    return render(request, "myadmin/info.html", context)

# ------------------后台商品信息管理------------------------
# 商品信息的页面
def goodsindex(request, pIndex=1):
    # 执行数据查询，并放置到模版中
    list = Goods.objects.all()
    for ob in list:
        ty = Types.objects.get(id=ob.typeid)
        ob.typename = ty.name # 判断并封装搜索条件
    # 传入数据和页大小来创建分页对象
    p = Paginator(list, 4)
    # 判断页号码没有值时，初始化为1
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex) # 类型转换int
    list2 = p.page(pIndex) # 获取当前页数据
    plist = p.page_range # 获取页面信息
    # 封装分页信息
    context = {'goodslist': list2, 'plist': plist, 'pIndex': pIndex}
    return render(request, "myadmin/goods/index.html", context)

# 商品信息添加
def goodsadd(request):
    # 获取商品类别信息
    # mysql版本时使用格式：list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    list = Types.objects.extra(select={'_has': 'path || id'}).order_by('_has')
    context = {'typelist': list}
    return render(request, "myadmin/goods/add.html", context)
def goodsinsert(request):
    try:
        # 判断并执行图片上传，缩放等处理
        # pic名称由前端页面设定
        myfile = request.FILES.get("pic",None)
        if not myfile:
            return HttpResponse("没有上传文件信息")
        # 以时间戳命名一个新图片名称
        filename = str(time.time())+"."+myfile.name.split('.').pop()
        # 打开文件
        destination = open(os.path.join("./static/goods/", filename), 'wb+')
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()
        # 执行图片缩放
        im = Image.open("./static/goods/"+filename)
        # 缩放到375*375
        im.thumbnail((375,375))
        # 把缩放为375的图片以jpeg格式保存
        im.save("./static/goods/"+filename, 'jpeg')
        # 缩放到220
        im.thumbnail((220,220))
        # 把缩放为220的图片以jpeg格式保存
        im.save("./static/goods/m_"+filename, 'jpeg')
        # 缩放到110
        im.thumbnail((110,110))
        # 把缩放为110后图片以JPEG格式保存
        im.save("./static/goods/s_"+filename, 'jpeg')

        # 获取商品信息并执行添加
        ob = Goods()
        ob.goods = request.POST['goods']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.descr = request.POST['descr']
        ob.picname = filename
        ob.state = 1
        ob.addtime = time.time()
        ob.save()
        context = {'info': '商品添加成功'}
    except:
        context = {'info': '商品添加失败'}
    return render(request, "myadmin/info.html", context)

# 商品信息删除
def goodsdel(request,gid):
    try:
        # 获取被删除商品信息量，先删除对应的图片
        ob = Goods.objects.get(id=gid)
        if ob.state == 1:
            # 1、执行图片删除
            os.remove("./static/goods/"+ob.picname)
            os.remove("./static/goods/m_"+ob.picname)
            os.remove("./static/goods/s_"+ob.picname)
            # 2、执行商品信息删除
            ob.delete()
            context = {'info': '商品删除成功'}
        else:
            context = {'info': '此状态不能删除'}
    except:
        context = {'info': '商品删除失败！！！'}
    return render(request, "myadmin/info.html", context)
# 商品信息编辑表单
def goodsedit(request,gid):
    try:
        # 获取要编辑的商品信息
        ob = Goods.objects.get(id=gid)
        # 获取商品的类别信息
        # mysql版本获取方式：list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
        list = Types.objects.extra(select={'_has': 'path || id'}).order_by('_has')
        # 放置信息加载模版
        context = {"typelist": list, 'goods': ob}
        return render(request, "myadmin/goods/edit.html", context)
    except:
        context = {'info': '没有找到要修改的商品信息'}
    return render(request, "myadmin/info.html", context)
# 商品信息更新页面
def goodsupdate(request,gid):
    try:
        b = False
        oldpicname = request.POST['oldpicname']
        if None != request.FILES.get('pic'):
            myfile = request.FILES.get('pic', None)
            if not myfile:
                return HttpResponse("更新编辑页面没有上传文件图片信息")
            # 以时间戳命名一个新图片名称
            filename = str(time.time())+"."+myfile.name.split('.').pop()
            destination = open(os.path.join("./static/goods/", filename), 'wb+')
            for chunk in myfile.chunks():
                destination.write(chunk)
            destination.close()
            # 执行图片缩放
            im = Image.open("./static/goods/" + filename)
            # 缩放到375*375:
            im.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/" + filename, 'jpeg')
            # 缩放到220*220:
            im.thumbnail((220, 220))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/m_" + filename, 'jpeg')
            # 缩放到220*220:
            im.thumbnail((100, 100))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/s_" + filename, 'jpeg')
            b = True
            picname = filename
        else:
            picname = oldpicname
        ob = Goods.objects.get(id=gid)
        ob.goods = request.POST['goods']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.descr = request.POST['descr']
        ob.picname = picname
        ob.state = request.POST['state']
        ob.save()
        context = {'info': '商品信息修改成功'}
        if b:
            os.remove("./static/goods/m_"+oldpicname) # 执行老图片删除
            os.remove("./static/goods/s_"+oldpicname) # 执行老图片删除
            os.remove("./static/goods/"+oldpicname) # 执行老图片删除
    except:
        context = {'info': '商品信息修改失败！！！'}
        if b:
            os.remove("./static/goods/m_"+picname) # 执行新图片删除
            os.remove("./static/goods/s_"+picname) # 执行新图片删除
            os.remove("./static/goods/"+picname) # 执行新图片删除
    return render(request, "myadmin/info.html", context)
    return render(request, "myadmin/info.html", context)

