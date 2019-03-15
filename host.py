'''
    Simples script to get host info.
'''

from urllib.request import urlopen
from socket import gethostbyaddr
import pprint
import json

def get_host_info():

	r = urlopen('https://ipinfo.io/')

	ipinfo = r.read().decode('utf-8')

	json_info = json.loads(ipinfo)

	try:
		json_info['hostname'] = gethostbyaddr(json_info['ip'])[0]
	except Exception as e:
		json_info['hostname'] = str(e)

	return json_info


if __name__ == "__main__":
	r = get_host_info()

	pprint.pprint(r)