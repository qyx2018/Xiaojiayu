import urllib.request
from urllib.error import URLError, HTTPError

req = urllib.request.Request('http://123.123')
try:
	response = urllib.request.urlopen(req)
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
else:
	pass