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

"""

#cd data

adb push misc/apexdata/com.android.wifi /data/misc/apexdata/
adb push misc/bluedroid /data/misc/
adb push app* /data/
adb push system /data/

#adb push does not push empty folders, so capture and create them after pushing
find -depth -type d -empty -printf 'mkdir -p "%p"\n' >sh ./empty-dirs.sh
adb push empty-dirs.sh /data
adb shell "/data/empty-dirs.sh"

#adb push/pull does not preserve permissions or timestamps, let's save the originals for application
find -depth -printf '%m:%U:%G:%T@:%A@:%p\n' >saved-permissions
adb push saved-permissions /data
adb shell
while IFS=$'\n': read -r mod user group tchg tacc file; do
	chown -- "$user:$group" "$file"
	chmod "$mod" "$file"
	touch -cm -d @$(echo "$tchg" | cut -d. -f1) "$file"
	touch -ca -d @$(echo "$tacc" | cut -d. -f1) "$file"
done <saved-permissions

"""