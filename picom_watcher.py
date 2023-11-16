#!/usr/bin/python
import subprocess
from time import sleep


watchout = ["Guild Wars 2","League of Legends","Riot Client"]
killpicom = False
while(1):
	for x in watchout:
		output1 = subprocess.Popen(["ps","aux"],stdout=subprocess.PIPE)
		output2 = subprocess.Popen(["grep",x],stdin=output1.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output1.stdout.close()
		out,err = output2.communicate()
		out = out.decode("utf-8")
		print(out)
		if len(out.split("\n")) > 2:
			killpicom = True
	if killpicom:
		subprocess.Popen(["killall","picom"])
		killpicom = False
	else:
		subprocess.Popen(["nohup","picom"])
	sleep(10)
