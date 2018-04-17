from urllib.request import Request, urlopen
from urllib.error import URLError

req = Request('http://1234.123.com')
try:
	response = urlopen(req)
except URLError as e:
	if hasattr(e, 'reason'):
		print('We failed to reach a server.')
		print('Reason: ', e.reason)
	elif hasattr(e, 'code'):
		print('The server couldm\'t fulfill the reqest.')
		print('Error code: ', e.code)
else:
	pass
