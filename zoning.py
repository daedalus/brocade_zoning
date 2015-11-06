#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import sys

def proc_json(filename):
	json_data = ''
	f = open(filename)
	#import ast
	import json
       	#j = ast.literal_eval(json_data)
	j = json.load(f)
	return j

def mkcfg(wwns,zoning,cfgs):

	txt = "cfgclear\n"

	for wwn in wwns:
		k = wwn.keys()	
		v = wwn.values()
		alias = "alicreate %s, %s" % (k[0],v[0])
		txt = txt + alias + "\n"

	for zone in zoning:
		k = zone.keys()
		v = zone.values()
		zone = 'zonecreate %s, "%s; %s"' % (k[0],v[0][0],v[0][1])
		txt = txt + zone + "\n"

	i = 0

	cfgname = cfgs.keys()[0]
	members = cfgs.values()[0]

	for member in members:
		if i == 0:
			cfg = "cfgcreate %s, %s" % (cfgname,member)
		else:
			cfg = "cfgadd %s, %s" % (cfgname,member)
		i+=1
		txt = txt + cfg + "\n"

	txt = txt + "cfgenable %s" % cfgname

	return txt

json = proc_json(sys.argv[1])
wwns = json['ALIAS']
zoning = json['ZONES']
cfgs = json['CFGS']

print mkcfg(wwns,zoning,cfgs)
