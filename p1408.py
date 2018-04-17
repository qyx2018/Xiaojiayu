import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

print('添加代理IP，多个IP地址间用英文的分号隔开！')

iplist = input('Please input IP: ').split(sep = ';')

while True:
	ip = random.choice(iplist)
	print(iplist)
	print(ip)
	proxy_support = urllib.request.ProxyHandler({'http':ip})
	opener = urllib.request.build_opener(proxy_support)
#	req.add_headers = ('Referer', 'http://www.youdao.com')
#	req.add_headers = ('User - Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
	urllib.request.install_opener(opener)
	
	try:
		print('In use %s' %ip)
		response = urllib.request.urlopen(url)
	except urllib.error.URLError:
		print('Error')
	else:
		print('Success')
	if input('Go on (Y/N)') == 'N':
		break


