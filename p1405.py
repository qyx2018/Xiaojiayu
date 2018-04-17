import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionForm=http://www.youdao.com/'
#url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=dict2.index'

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typeResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data)
req.add_header('Referer', 'http://www.youdao.com')
req.add_header('User - Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)
#print(target)
#print(target['translateResult'][0][0])
#print(req.headers)
print('翻译结果：%s' %(target['translateResult'][0][0]['tgt']))