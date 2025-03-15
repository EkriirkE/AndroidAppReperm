#!/usr/bin/env python
#--------========########========--------
#	Reset Android app permissions in the /data/data foler
#	2025-03-06	Erik Johnson - EkriirkE
#
#	Iterates the /data/system/packages.list file to get (and reset) the proper group permissions of each app folder
#	Run:
#	python reperm.py
#
#--------========########========--------
import os

if not (okgo:=os.path.exists(pkg:="/data/system/packages.list")):
	pkg="packages.list"
with open(pkg,"r") as f:
	while l:=f.readline():
		l=l.split(" ")
		if len(l)>10:continue
		l[3]=l[3].replace("/data/user/0/","/data/data/")
		cmd=f"chown -R {l[1]}:{l[1]} {l[3]}"
		print(cmd)
		if okgo:os.system(cmd)
		if x:=[x for x in [l[3]+"/cache",l[3]+"/code_cache"] if os.path.exists(x)]:
			cmd=f"chgrp -R {int(l[1])+10000} {' '.join(x)}"
			print(cmd)
			if okgo:os.system(cmd)
print("Done.")
