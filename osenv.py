# -*- coding: UTF-8 -*-
import platform

class osenv():
	def __init__(self):
		pass

	def getip(self):
		import socket
		ip = socket.gethostbyname(socket.gethostname())
		return ip

	def getmac(self):
		import uuid
		node = uuid.getnode()
		mac = uuid.UUID(int = node).hex[-12:]
		return mac

	def getarch(self):
		return platform.architecture()

	def getplatform(self):
		return platform.platform()

	def getsystem(self):
		return platform.system()

def test():
	os = osenv()
	print os.getip()
	print os.getmac()
	print os.getarch()
	print os.getplatform()
	print os.getsystem()

if __name__ == '__main__':
	test()
