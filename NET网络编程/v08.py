# HTML格式邮件案例
import smtplib
from email.mime.text import MIMEText
mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1> 这是一封HTML格式邮件</h1>
        </body>
        </html>
        """
'''
MIMEText三个参数
1、邮件内容
2、MIME子类型，在此案例我们用plain表示text类型
3、邮件编码格式
'''
msg = MIMEText("mail_content", "html", "utf-8")
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
