from send_message import tools

url = "http://gw.api.taobao.com/router/rest"  # 这是线上环境 沙箱环境请选择http://gw.api.tbsandbox.com/router/rest 具体内容去https://api.alidayu.com/doc2/apiDetail?spm=a3142.7629140.1.19.Woa50O&apiId=25450看
app_key = "你的app_key 大概是8位数字"
secret = "你的secret 很长的那个"

t = tools(url, app_key, secret)

sms_free_sign_name = "注册验证"  # 你的签名
sms_template_code = "SMS_7495113"  # 短信模板编号
sms_param = {"product": "123", "code": "123"}  # 给一个字典对象就可以 根据你的模板来
rec_num = "13000000000"  # 对应电话号码

t.set_para(sms_free_sign_name, sms_param, rec_num, sms_template_code)
text = t.send_message()
print(text)
