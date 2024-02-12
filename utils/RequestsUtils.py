# get封装
import requests

#封装get方法
def requests_get(url,header):
    # 发送请求
    r = requests.get(url,headers=header)
    # 获取响应内容
    code = r.status_code
    try:
        body = r.text
    except Exception as e:
        body = r.json()
    # 保持内容到字典
    data = {"code": code, "body": body}
    return data
#封装post方法
def requests_post(url,data,header):
    r=requests.post(url,headers=header,json=data)
    #获取响应内容
    code=r.status_code
    try:
        body=r.json()
    except Exception as e:
        body=r.text
    #内容存储到字典
    all=dict()
    all["code"]=code
    all["body"]=body
    return all
