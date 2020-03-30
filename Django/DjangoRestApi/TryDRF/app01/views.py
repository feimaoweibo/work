from django.shortcuts import render
from app01 import models
from django.http import HttpResponse

# Create your views here.
def publisher_list(request):
    # 拿出所有的数据
    queryset = models.Publisher.objects.all()

    '''方法一
    # 设置一个data空列表
    data = []
    for i in queryset:
        # 中间变量 p_tmp,所有的数据手动转换为字典
        p_tmp = {
            "name": i.name,
            "address": i.address
        }
        # 把转换为字典后的数据，放入data列表
        data.append(p_tmp)
    import json
    # 使用json.dumps来把data列表内容转换为字符串格式内容，content_type为指定的json格式
    return HttpResponse(json.dumps(data), content_type="application/json")
    '''

    '''方法二 图片、网址字段不能上传
    # 设置一个data空列表
    data = []
    from django.forms.models import model_to_dict
    for i in queryset:
        data.append(model_to_dict(i))
    import json
    # 使用json.dumps来把data列表内容转换为字符串格式内容，content_type为指定的json格式
    return HttpResponse(json.dumps(data), content_type="application/json")
    '''

    '''
    # 方法三 使用django自带的serializers（序列化）
    from django.core import serializers
    data = serializers.serialize("json",queryset)
    import json
    return HttpResponse(data, content_type="application/json")

    '''
    # 方法四
    from app01 import serializers
    serializer = serializers.PublisherSerializer(queryset, many=True) #queryset表示所有数据，many=True表示有多个
    import json
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")
