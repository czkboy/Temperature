import requests
from bs4 import BeautifulSoup as bs
import time

def now_to_timestamp(digits = 10):
    time_stamp = time.time()
    digits = 10 ** (digits -10)
    time_stamp = int(round(time_stamp*digits))
    return time_stamp

def login():
    login_url = 'http://xscfw.hebust.edu.cn/survey/ajaxLogin'
    headers = {
        "Accept": "application/json, text/javascript"
    }
    body = {
        "stuNum": "180705136",
        "pwd": "Lipai2323#000229"
    }
    try:
        res = requests.post(url=login_url, headers=headers, data=body)
        cookies = res.cookies

        cookie = requests.utils.dict_from_cookiejar(cookies)

        return cookie
    except Exception as err:
        print('获取cookie失败：\n{0}'.format(err))








def Tianbao():
    cookie = login()['JSESSIONID']
    index_url = "http://xscfw.hebust.edu.cn/survey/index"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.8","cookie":"JSESSIONID="+cookie
    }


    res = requests.post(url=index_url, headers=headers)
    soup = bs(res.text, 'html.parser')
    sid=soup.select('li.mdui-list-item.mdui-list-item')[0].attrs['sid']

    tianbao_url="http://xscfw.hebust.edu.cn/survey/surveySave"
    body = {
        "id":sid,
        "stuId" : 25756,
        #"qid":22954,
        "c0":"不超过37.3℃，正常",
        "c1" : 36.1,
        "c3":"不超过37.3℃，正常",
        "c4" : 36.1,
        "c6" : "健康"
    }
    requests.post(url=tianbao_url, headers=headers, data=body)
    res=requests.post(url=index_url, headers=headers)
    soup = bs(res.text, 'html.parser')
    Text=soup.select('span.list-checked.mdui-float-right')[0].get_text()
    if(Text=="已完成"):
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),Text)
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "未完成")



Tianbao()