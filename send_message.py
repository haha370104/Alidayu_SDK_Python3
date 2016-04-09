# coding=utf-8
import top.api


class tools:
    req = None

    def __init__(self, url, app_key, secret):
        self.req = top.api.AlibabaAliqinFcSmsNumSendRequest(url)
        self.req.set_app_info(top.appinfo(app_key, secret))

    def set_para(self, sms_free_sign_name, sms_param, rec_num, sms_template_code):
        self.req.extend = "123456"
        self.req.sms_type = "normal"
        self.req.sms_free_sign_name = sms_free_sign_name
        self.req.sms_param = str(sms_param)
        self.req.rec_num = rec_num
        self.req.sms_template_code = sms_template_code

    def send_message(self):
        try:
            resp = self.req.getResponse()
            return resp
        except Exception as e:
            return e
