#!/usr/bin/python3

import configparser
from pymongo import MongoClient

#
#	settings.cfg and helpers
#

S = configparser.ConfigParser()
S.read('settings.cfg')

def get(*args,**kwargs):
	return S.get(*args,**kwargs)

def getint(*args,**kwargs):
	return S.getint(*args,**kwargs)

def getboolean(*args,**kwargs):
	return S.getboolean(*args,**kwargs)

#
#	mongodb stuff
#

mdb = MongoClient().toconnell_info.v3
