# 多线程概述
'''
-工作环境
     win10 64λ
     anaconda
     pycharm
     python3.6
     https://www.cnblogs.com/jokerbj/p/7460260.html
     http://www.dabeaz.com/python/UnderstandingGIL.pdf
'''
# 多线程与多进程
'''
-程序：一堆代码以文本形式存入一个文档
-进程： 程序运行的一个状态
    包含地址空间，内存，数据栈等
    每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
-线程
    一个进程的独立运行片段，一个进程可以由多个线程
    轻量化的进程
    一个进程的多个线程间共享数据和上下文运行环境
    共享互斥问题
-全局解释器锁（GIL）
    Python代码的执行是由python虚拟机进行控制
    在主循环中稚嫩更有一个控制线程在执行
-Python包
    thread：有问题，不好用，python3改成了_thread
    threading: 通行的包,目前python3版本使用
    案例01: 顺序执行，耗时比较长
    案例02： 改用多线程，缩短总时间，使用_thread
    案例03： 多线程，传参数
-threading的使用
    直接利用threading.Thread生成Thread实例
        t = threading.Thread(target=xxx, args=(xxx,))
        t.start():启动多线程
        t.join(): 等待多线程执行完成
        案例04
        案例05: 加入join后比较跟案例04的结果的异同
        守护线程-daemon
            如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
            一般认为，守护线程不重要或者不允许离开主线程独立运行
            守护线程案例能否有效果跟环境相关
            案例06非守护线程
            案例07守护线程
        线程常用属性
            threading.currentThread：返回当前线程变量
            threading.enumerate:返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动后，结束前的状态
            threading.activeCount: 返回正在运行的线程数量，效果跟 len(threading.enumerate)相同
            thr.setName: 给线程设置名字
            thr.getName: 得到线程的名字
            案例08   
    直接继承自threading.Thread
        直接继承Thread
        重写run函数
        类实例可以直接运行
        案例09
        案例10， 工业风案例    
-共享变量
    共享变量： 当多个线程同时访问一个变量的时候，会产生共享变量的问题
    案例11
    解决变量：锁，信号灯，
    锁（Lock）：
        是一个标志，表示一个线程在占用一些资源
        使用方法
            上锁
            使用共享资源，放心的用
            取消锁，释放锁
        案例12
        锁谁： 哪个资源需要多个线程共享，锁哪个
        理解锁：锁其实不是锁住谁，而是一个令牌        
'''