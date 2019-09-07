# 添加邮件头、抄送等信息案例
import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("hello world", "plain", "utf-8")
# 填写发送者信息
header_from = Header("从图灵学院邮箱发出去的<tulingxueyuan@qq.cn>", "utf-8")
msg['From'] = header_from
# 填写接收者信息
header_to = Header("去王晓静的地方<wangxiaojing@sina.com>", 'utf-8')
# 添加抄送主题
header_sub = Header("这是图灵学院的主题", 'utf-8')
msg['Subject'] = header_sub

# 发送Email地址，此次地址使用刘大拿的QQ邮箱，密码一般需要临时输入，此处偷懒
from_addr = "1366798119@qq.com"
# 此处密码是经过申请设置后的授权码，不是使用QQ邮箱的密码
from_pwd = "hjpovygcxmrshhcj"
# 收件人信息
to_addr = "531148362@qq.com"
'''
输入SMTP服务器地址:
# 此处根据不同的邮件服务商有不同的值，
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱所的smtp地址是 smtp.qq.com
'''
smtp_srv = "smtp.qq.com"
try:
    # 连个参数：1）是服务器地址，但一定是bytes格式，需要编码；2）是服务器的接受访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)# SMTP协议默认端口是25
    # 登陆邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件的三个参数
    '''
    1、发送地址
    2、接收地址，必须是list形式
    3、发送内容，作为字符串发送
    '''
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    # 退出邮箱
    srv.quit()
except Exception as e:
    print(e)