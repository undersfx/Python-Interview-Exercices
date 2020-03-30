'''
    Simple script to get host info.
'''

from urllib.request import urlopen
import socket
import pprint
import json


def get_host_info():

	r = urlopen('https://ipinfo.io/')

	ipinfo = r.read().decode('utf-8')

	response = json.loads(ipinfo)

	try:
		response['hostname'] = socket.gethostbyaddr(response['ip'])[0]
	except socket.herror as e:
		response['hostname'] = 'NXDOMAIN'

	return response


if __name__ == "__main__":
	r = get_host_info()
	pprint.pprint(r)