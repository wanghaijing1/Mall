#!usr/bin/python
# _*_coding:utf-8_*_
import base64
from io import BytesIO

import requests
import time

from PIL import Image

access_key = 'qoIEAS7DCNwo5tYfL4BMt0HO'
secret_key = 'mQWLnTkCbEmuwM8bgcpGCGoVotU5gbDR'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           # 'Cookie': 'gr_user_id=6b6ca854-d577-43ee-9649-2b4fc0b47774; JSESSIONID=5D06EC423FBFED305F44EE36A1001CAD; Hm_lvt_7f1c38424a58e6ebb23eeee705ad45af=1527578584,1527579058,1527586641,1527679370; nb-referrer-hostname=www.edianzu.com; nb-start-page-url=https%3A%2F%2Fwww.edianzu.com%2Flogin%3FreturnUrl%3Dhttps%253A%252F%252Fwww.edianzu.com%252F; gr_session_id_a5524122e79c5822=843bc141-4cd1-48a3-bc3e-ead4c7473ffd_true; Hm_lpvt_7f1c38424a58e6ebb23eeee705ad45af=1527683249',
           'Host': 'www.edianzu.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
           }

count = 0


# 获取验证码图片并识别，返回结果
def get_chaptcha_image(request_url):
    try:
        response = requests.get(request_url, headers=headers, timeout=1)
        if response.status_code == 200:
            # Image.open()  打开文件路径下的图片
            captcha = Image.open(BytesIO(response.content))
            image = base64.b64encode(BytesIO(response.content).read())
            word = check_captcha_img(image)
            return word
    except TimeoutError as e:
        print('响应超时---')
        time.sleep(1)
        return get_chaptcha_image(request_url)


# 调用接口识别验证码
def check_captcha_img(re_image):
    # request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
    request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    acc_token = get_baidu_token(access_key, secret_key)
    re_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # img = open('/data/test_captcha/1_captcha.jpg', 'rb')
    # re_image = base64.b64encode(img.read())
    # img.close()
    re_data = {'access_token': acc_token,
               'image': re_image}
    response = requests.post(request_url, data=re_data, headers=re_headers)
    if response.status_code == 200:
        words_result = response.json()['words_result']
        word = [x['words'] for x in words_result]
        print(word[0])
        return word[0]
    else:
        print('请求失败--！')
        return None


# 获取接口access_token
def get_baidu_token(access_key, secret_key):
    request_data = {'grant_type': 'client_credentials',
                    'client_id': access_key,
                    'client_secret': secret_key
                    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    baidu_token_url = 'https://aip.baidubce.com/oauth/2.0/token'

    try:
        baidu_response = requests.post(baidu_token_url, data=request_data, headers=headers)
        if baidu_response.status_code == 200:
            re_json = baidu_response.json()
            # print(re_json['access_token'])
            return re_json['access_token']
        else:
            print('获取access_token响应不为200：{}'.format(baidu_response.status_code))
    except BaseException as e:
        print('获取access_token异常')
        raise e


if __name__ == '__main__':
    captcha_url = 'https://www.edianzu.com/getCaptcha?count=5&amp;t=Thu May 31 2018 18:42:09 GMT+0800 (中国标准时间)'
    word = get_chaptcha_image(captcha_url)
    print('word: {}'.format(word))
