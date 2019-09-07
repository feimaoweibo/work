# 发送带有附件的邮件案例
import smtplib
from email.mime.text import MIMEText #构建附件使用
from email.mime.multipart import MIMEBase, MIMEMultipart #构建基础邮件使用
mail_mul = MIMEMultipart()
# 构建邮件正文
mail_text = MIMEText("这是带附件格式的邮件的正文文本内容", "plain", "utf-8")
# 把构建好的邮件正文附加入邮件中
mail_mul.attach(mail_text)

# 构建附件
'''
构建附件，需要从本地读入文件
打开一个本地文件，以rb格式打开
'''
with open("02.html", 'rb') as f:
    s = f.read()
    # 设置附件的MIME和文件名
    m = MIMEText(s, 'base64', 'utf-8')
    m['Content-type'] = 'application/octet-stream'
    '''
    需要注意：
    1、attachment后分号为英文状态
    2、filename后面需要用引号包裹，注意与外面引号错开
    '''
    m['Content-Dispoition'] = "attachment; filename='02.html'"
    # 添加到MIMEMultipart
    mail_mul.attach(m)

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
    srv.sendmail(from_addr, [to_addr], mail_mul.as_string())
    # 退出邮箱
    srv.quit()
except Exception as e:
    print(e)