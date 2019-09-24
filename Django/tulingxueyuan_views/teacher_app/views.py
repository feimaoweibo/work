from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def teacher(req):
    return HttpResponse("这是teacher的一个视图")

def v2_exception(r):
    raise Http404
    return HttpResponse("OK")

def v10_1(request):
    return HttpResponseRedirect('/v11')
def v10_2(request):
    return HttpResponseRedirect(reverse("v11")),
def v11(request):
    return HttpResponse("哈哈，这是v11的访问返回内容")

def v8_get(request):
    rst = ""
    for k,v in request.GET.items():
        # 采用键值对字典格式
        rst = rst + k + "--->" + v
        rst += ","
    return HttpResponse("Get value of Request is {0}".format(rst))

def v9_get(request):
    # 渲染模版并返回
    return render_to_response('for_post.html')
def v9_post(request):
    rst = ''
    for k,v in request.POST.items():
        rst += k + "---->" + v
        rst += "，"
    return HttpResponse("Post value of POST is {0}".format(rst))

def render_test(request):
    rsp = render(request, "render.html")
    return rsp
def render2_test(request):
    # 环境变量
    c = dict()
    c["name"] = "LiuDana"
    c["name2"] = "LiuErna"
    c["name3"] = "LiuSanna"
    rsp = render(request, "render2.html", context=c )
    return rsp
def render3_test(request):
    from django.template import loader
    # 得到模版
    t = loader.get_template("render2.html")
    print(type(t))
    r = t.render({"name": "LIUDANA"})
    print(type(r))
    return HttpResponse(r)
def render_to_request(request):
    # 反馈回渲染模版render2.html
    rsp = render_to_response("render2.html", context={"name": "WangDaMei"})
    return rsp

def get404(request):
    # 系统内建视图，可以直接使用，
    # 例子default.page_not_found(request, template_name='404.html')
    from django.views import defaults
    return defaults.page_not_found(request, template_name="render.html")
