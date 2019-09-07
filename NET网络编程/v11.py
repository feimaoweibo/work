# 同时支持HTML和text格式邮件案例
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 构建一个MIMEMultipart邮件
msg = MIMEMultipart("alternative")
# 构建一个HTML邮件内容
html_content = """
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
msg_html = MIMEText(html_content, "html", "utf-8")
msg.attach(msg_html)

# 构建text文本内容
msg_text = MIMEText("这是文本部分内容示例", "plain", 'utf-8')
msg.attach(msg_text)

# 发送email地址，此处地址直接使用我的qq邮箱，密码临时输入
from_addr = "1366798119@qq.com"
#from_pwd = input('163邮箱密码: ')
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
    # 加密传输
    # server = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口是25
    # qq邮箱要求使用 TLS加密传输
    server = smtplib.SMTP(smtp_srv.encode(), 25)  # SMTP协议默认端口是25
    server.starttls()
    # 设置调试级别，通过不同调试等级，可以清楚的看到发送邮件的交互步骤
    server.set_debuglevel(1)
    # 登录发送邮箱
    server.login(from_addr, from_pwd)
    # 发送邮件的三个参数
    '''
    1、发送地址
    2、接收地址，必须是list形式
    3、发送内容，作为字符串发送
    '''
    server.sendmail(from_addr, [to_addr], msg.as_string())
    # 退出登陆
    server.quit()
except Exception as e:
    print(e)