import urllib.request
import urllib.parse
import json

url = 'http://www.whatismyip.com.tw'
proxy_support = urllib.request.ProxyHandler({'http':'223.158.250.58:8118'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')
print(html)

#target = json.loads(html)

#print('翻译结果：%s' %(target['translateResult'][0][0]['tgt']))


