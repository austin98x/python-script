# -*- coding: UTF-8 -*-
import os
import os.path
import sys
import subprocess
import threading
import time
import logging
import logging.handlers
import csv
import traceback

class Logger():
	def __init__(self):
		self.logger = logging.getLogger('auto') # get instance
		self.logger.setLevel(logging.DEBUG) # NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
		#%(name)s
		#%(levelno)s
		#%(levelname)s
		#%(pathname)s
		#%(filename)s
		#%(module)s
		#%(funcName)s
		#%(lineno)d
		#%(created)f
		#%(relativeCreated)d 
		#%(asctime)s
		#%(thread)d
		#%(threadName)s
		#%(process)d
		#%(message)s
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - line %(lineno)s - %(message)s')

		# output to console
		handler = logging.StreamHandler()
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)

		# write to file
		handler = logging.handlers.RotatingFileHandler('auto.log', maxBytes = 1024*1024, backupCount = 5)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def warning(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.error(message)

	def critical(self, message):
		self.logger.critical(message)

def test():
	log = Logger()
	log.debug("debug message")
	log.info("info message")
	log.warning("warning message")
	log.error("error message")
	log.critical("critical message")

if __name__ == '__main__':
	test()
