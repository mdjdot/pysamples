#!/usr/bin/env python3

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20190711 import sms_client, models

from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


def sendSMS(code, due):
    try:
        # CAM密匙查询: https://console.cloud.tencent.com/cam/capi
        cred = credential.Credential(
            "*********", "*********")
        # cred = credential.Credential(
        #     os.environ.get(""),
        #     os.environ.get("")
        # )

        req = models.SendSmsRequest()

        # 实例化要请求产品(以sms为例)的client对象
        # 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量
        client = sms_client.SmsClient(cred, "ap-shanghai")

        # 帮助链接：
        # 短信控制台: https://console.cloud.tencent.com/sms/smslist
        # sms helper: https://cloud.tencent.com/document/product/382/3773

        # 短信应用ID: 短信SdkAppid在 [短信控制台] 添加应用后生成的实际SdkAppid，示例如1400006666
        req.SmsSdkAppid = "0000000000"

        # 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看
        req.Sign = "腾讯云"

        # 短信码号扩展号: 默认未开通，如需开通请联系 [sms helper]
        req.ExtendCode = ""

        # 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回
        req.SessionContext = "xxx"

        # 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号]
        # 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号
        req.PhoneNumberSet = ["+8611111111111"]

        # 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看
        req.TemplateID = "555555"

        # 模板参数: 若无模板参数，则设置为空
        req.TemplateParamSet = [code, due]

        # 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的。
        # 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应。

        resp = client.SendSms(req)

        # 输出json格式的字符串回包
        return resp.to_json_string(indent=2)

    except TencentCloudSDKException as err:
        print(err)
        return ""


if __name__ == "__main__":
    sendSMS("********", 5)
