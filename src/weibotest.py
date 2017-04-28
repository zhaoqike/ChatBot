# -*- coding: utf8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys   #引用sys模块进来，并不是进行sys的第一次加载
reload(sys)  #重新加载sys
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数
import collections
import json

from weibo import APIClient
import webbrowser#python内置的包
import random
import time

APP_KEY = '3224840065'
APP_SECRET = '8b1e89544dff3fe8822a118c836a11c9'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

#利用官方微博SDK
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
#得到授权页面的url，利用webbrowser打开这个url
url = client.get_authorize_url()
print url
webbrowser.open_new(url)
#获取code=后面的内容
print '输入url中code后面的内容后按回车键：'
code = raw_input()
#code = your.web.framework.request.get('code')
#client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in
# 设置得到的access_token
client.set_access_token(access_token, expires_in)


def wait_random():
    t = random.uniform(5, 10)
    time.sleep(t)

def append_text(path, text):
    f = open(path,'a')
    f.write(text+u'\n')
    f.close()


def grab_page(page_num):
    wait_random()
    timeline = client.statuses__public_timeline(page=page_num, count=200)
    statuses = timeline['statuses']
    length = len(statuses)
    print "page: ", page_num, "length: ", length
    print json.dumps(timeline, ensure_ascii=False)
    #输出了部分信息
    for si in range(0,length):
        print u'id:'+str(statuses[si]['id'])
        print u'text:'+statuses[si]['text']

        commlist = []
        wait_random()
        comments = client.comments__show(id=statuses[si]['id'])['comments']
        for ci in range(0, len(comments)):
            print u'comment:'+comments[ci]['text']
            commlist.append(comments[ci]['text'])
        d = collections.OrderedDict()
        d['id'] = statuses[si]['id']
        d['text'] = statuses[si]['text']
        d['comments'] = commlist
        append_text('/home/zhaoqike/weibotext.txt', json.dumps(d, ensure_ascii=False))


for i in range(1, 10):
    print 'page: ', i
    grab_page(i)