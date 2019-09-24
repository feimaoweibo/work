# Django框架 概述
    - 环境
        python3.7
        django1.8
    - 参考资料
        django中文教材：http://python.usyiyi.cn/
        django架站的16堂课
# 环境搭建
    - annconda + pycharm
    - annconda使用
        conda list: 显示当前环境安装的包
        conda env list: 显示安装的虚拟环境列表
        conda create -n env_name python=3.7
        激活conda的虚拟环境
            Linux：source activate env_name
            Win：activate env_name
        pip install django=1.8
# 一、创建第一个django程序
    - 命令行启动
        django-admin startproject tulingxueyuan
        cd tulingxueyuan
        python manage.py runserver
    - pycharm启动
        - 需要配置
### 1、路由系统-urls
    - 创建app
        app：负责一个具体业务或者一类具体业务的模块
        python manage.py startapp teacher
    - 路由
        按照具体的请求url，导入到相应的业务处理模块的功能
        django的信息控制中枢
        在本质上接受的URL和相应的处理模块的一个映射
        在接受URL请求的匹配上使用RE（正则表达式）
        URL的具体格式在urls.py中所示
    - 需要关注2点：
        1）接受URL是什么，即如何用RE对传入的URL进行匹配
        2）已知URL匹配到哪个处理模块
    - URL匹配规则
        从上往下一个一个比对
        url格式是分级格式，则按照级别一级一级往下比对,主要对应url包含子url的情况
        子url一旦被调用，则不会返回到主url
            /one/two/three/
        正则以r开头,表示不需要转义，注意尖号(^)和美元符号($)
            /one/two/three 配对 r'^one/
            /oo/one/two/three 不配对 r'^one/"
            /one/two/three/ 配对 r'three/$'
            /oo/one/two/three/oo/ 不配对 r'three/$"
            开头不需要有反斜杠
        如果从上向下都没有找到合适的匹配内容，则报错
### 2、正常映射
    把某一个符合RE的URL映射到事物处理函数中去
        举例如下:
            from showeast import views as sv
            
            urlpatterns = [
                url(r'^admin/', admin.site.urls),
                url(r'^normalmap/', sv.normalmap),
            ]
### 3、URL中带参数映射
    在事件处理代码中需要由URL传入参数,形如 /myurl/param中的param
    参数都是字符串形式,如果需要整数等形式需要自行转换
    通常的形式如下:
          /search/page/432 中的 432需要经常性变换，所以设置成参数比较合适
### 4、URL在app中处理
    如果所有应用URL都集中tulingxueyuan/urls.py中,可能导致文件的臃肿
    可以把urls具体功能逐渐分散到每个app中
        从django.conf.urls 导入 include
        注意此时RE部分的写法
        添加include导入
    使用方法
        1确保include被导入
        2写主路由的开头url
        3写子路由
        4编写views函数
    同样可以使用参数
### 5、URL中嵌套参数
    捕获某个参数的一部分
    例如URL/index/page-3,需要捕获数字3作为参数
        url(r'index_1/(page-(\d+)/)?$', sv.myindex_1), #不太好
        url(r'index_2/(?:page-(?P<page_number>\d+)/)?$', sv.myindex_2), #好
    上述例子会得到两个参数，但?:表明忽略此参数
### 6、传递额外参数
    参数不仅仅来之以URL，还可能是我们自己定义的内容
        url(r'extrem/$', tv.extremParam, {'name':"liuying"}),
    附加参数同样适用于include语句,此时对include内所有都添加
### 7、URL的反向解析
    防止硬编码
    本质上是对每一个URL进行命名
    以后在编码代码中使用URL的值，原则上都应该使用反向解析    
    
# 二、视图views
### 1、视图概述
    视图即视图函数，接受web请求并返回web响应的事物处理函数
    相应指符合http协议要求的任何内容，包括json,string,html等
    本章忽略事物处理，重点在如何返回处理结果上
### 2、其他简单视图
    django.http给我们提供了很多和HttpResponse类似简单视图，通过查django.http代码查询
    此类视图使用方法基本类似，可以通过return语句，直接反馈返回结果给客户端浏览器
    Http404为Exception子类，所以需要raise使用
### 3、HttpResponse详解
    方法：
        init ：使用页内容实例化HttpResponse对象
        write(content)：以文件的方式写
        flush()：以文件的方式输出缓存区
        set_cookie(key, value='', max_age=None, expires=None)：设置Cookie
            key,value都是字符串类型
            max_age是一个整数，表示在指定秒数后过期
            expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
            max_age与expires二选一
            如果不指定过期时间，则两个星期后过期
        delete_cookie(key)：删除指定的key的Cookie，如果key不存在则什么也不发生
### 4、HttpResponseRedirect
    重定向，服务器端跳转
    构造函数的第一个参数用来制定重定向的地址
    案例ShowViews/views.py
        # 在/urls中添加一下内容
        url(r'^v10_1/', views.v10_1),
        url(r'^v10_2/', views.v10_2),
        url(r'^v11/', views.v11, name="v11"),
        
        # 在/views中添加一下内容
        def v10_1(request):
            return HttpResponseRedirect("/v11")
        
        def v10_2(request):
            return HttpResponseRedirect(reverse("v11"))
        
        def v11(request):
            return HttpResponse("哈哈，这是v11的访问返回呀")
### 5、Request对象
    Request介绍
        服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
        视图函数的第一个参数是HttpRequest对象
        在django.http模块中定义了HttpRequest对象的API
    属性
        下面除非特别说明，属性都是只读的
        path：一个字符串，表示请求的页面的完整路径，不包含域名
        method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
        encoding：一个字符串，表示提交的数据的编码方式
            如果为None则表示使用浏览器的默认设置，一般为utf-8
            这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
        GET：一个类似于字典的对象，包含get请求方式的所有参数
        POST：一个类似于字典的对象，包含post请求方式的所有参数
        FILES：一个类似于字典的对象，包含所有的上传文件
        COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串
        session：一个既可读又可写的类似于字典的对象，表示当前的会话
            只有当Django 启用会话的支持时才可用，
            详细内容见“状态保持”
    方法
        is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True
    QueryDict对象
        定义在django.http.QueryDict
        request对象的属性GET、POST都是QueryDict类型的对象
        与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
        方法get()：根据键获取值
            只能获取键的一个值
            如果一个键同时拥有多个值，获取最后一个值
        方法getlist()：根据键获取值
            将键的值以列表返回，可以获取一个键的多个值
    GET属性
        QueryDict类型的对象
        包含get请求方式的所有参数
        与url请求地址中的参数对应，位于?后面
        参数的格式是键值对，如key1=value1
        多个参数之间，使用&连接，如key1=value1&key2=value2
        键是开发人员定下来
        案例/views/v8_get
            http://127.0.0.1:8000/v8/?fristName=liu&lastName=ying&addr=beijing
    POST属性
        QueryDict类型的对象
        包含post请求方式的所有参数
        与form表单中的控件对应
        表单中空间必须有name属性，name为键，value为值
            checkbox存在一键多值的问题
        键是开发人员定下来的，值是可变的
        案例/views/v9_post
            settings中设置模板位置(已经设置完毕)
            设置get页面的urls和函数
                # tulingxueyuan_views/urls.py
                # 需要在路由文件中添加两个路由
                url(r'^v9_get/', views.v9_get),
                url(r'^v9_post/', views.v9_post),
                 # teacher_app/views.py
                 # 在文件中添加下面两个处理函数
                def v9_get(request):
                    return  render_to_response("for_post.html")
            
                def v9_post(request):
                    rst = ""
                    for k,v in request.POST.items():
                        rst += k + "-->" + v
                        rst += ","
            
                    return HttpResponse("Get value of POST is {0} ".format(rst))
            添加文件/templates/for_post.html
            由于安全原因，需要在设置中安全选项中删除csrf设置
                # settings.py
                MIDDLEWARE = [
                    'django.middleware.security.SecurityMiddleware',
                    'django.contrib.sessions.middleware.SessionMiddleware',
                    'django.middleware.common.CommonMiddleware',
                      #  下面这句话被注释掉
                    #'django.middleware.csrf.CsrfViewMiddleware',
                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                    'django.contrib.messages.middleware.MessageMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                ]
    手动编写视图
        实验目的：
            利用django快捷函数手动编写视图处理函数
            编写过程中理解视图函数运行原理
        分析：
            django把所有请求信息封装入request
            django通过urls模块把相应的请求根事件处理函数链接起来，并把request作为参数传入
            在相应的处理函数中，我们需要完成两部分
                处理业务
                把结果封装并返回，我们可以使用简单HttpResponse，同样也可以自己处理此功能，例如本例子
            本例子不介绍业务处理，把目光集中在如何渲染结果并返回
        render(request, template_name[, context][, context_instance][, content_type][, status][, current_app][, dirs][, using])
            使用模版和一个给定的上下文环境，返回一个渲染和HttpResponse对象
            request:django的传入请求
            template_name:模版名称
            content_instance:上下文环境
            案例参看代码 teacher_app/views/render_test
        render_to_response
            根据给定的上下文字典渲染给定模版，返回渲染后的HttpResponse    
    系统内建视图
        系统内建视图，可以直接使用        
        404       
            default.page_not_found(request, template_name='404.html')
            系统引发Http404时出发
            默认船体request_path变量给模板,即导致错误的URL
            DEBUG=True则不会调用404, 取而代之是调试信息
            404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量(MEDIA_URL等)
        500(server error)      
            defaults.server_error(request, template_name='500.html')
            需要DEBUG=False,否则不调用
        403 (HTTP Forbidden) 视图       
            defaults.permission_denied(request, template_name='403.html')
            通过PermissionDenied触发
        400 (bad request) 视图       
            defaults.bad_request(request, template_name='400.html')
            DEBUG=False        