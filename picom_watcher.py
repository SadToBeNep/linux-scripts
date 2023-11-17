#!/usr/bin/python

import json
import subprocess
from time import sleep
from os import mkdir,path

class ConfigFile():
	BASIC_CONFIG = '{"watchout_list": ["Guild Wars 2", "League of Legends", "Riot Client"], "sleep_time": 15, "compozitor": "picom", "config_location": "~/.config/pi_watch/config"}'

	def __init__(self, watchout_list=["Guild Wars 2", "Riot Client", "League of Legends"], sleep_time=10, compozitor="picom", config_location="~/.config/pi_watch/config"):
		self.watchout_list = watchout_list
		self.sleep_time = sleep_time
		self.compozitor = compozitor
		self.config_location = config_location\
	
	def GetUsername(self):
		username = subprocess.run(["whoami"], text=True, capture_output=True, check=False)
		return username.stdout
	
	def OpenConfigFile(self):
		try:
			ConfigContents = self.ReadConfigFile()
			self.__dict__ == json.loads(ConfigContents)

		except FileNotFoundError:
			print(f"No config file was found at {self.config_location}\nDo you want to create one? [Y/n]")
			answer = str(input())
			if answer.lower() == "y":
				self.CreateConfigFile()
			else:
				print("[ERR] No config file found, exit")
				exit(404)
		self.OpenConfigFile()
			
	def CreateConfigFile(self):
		CreateDir = True
		print("[DEB] Trying to create directory for config file")
		Username = self.GetUsername().strip()
		if((path.exists(f"/home/{Username}/.config/pi_watch")) == True):
			print("[DEB] Directory already exists")
			CreateDir = False
		else:
			MakeDir = mkdir(f"/home/{Username}/.config/pi_watch")
		if((path.exists(f"/home/{Username}/.config/pi_watch")) == False):
			print("[ERR] Error while trying to create config directory")
		else:
			process = subprocess.run(["touch",f"/home/{Username}/.config/pi_watch/config"],check=False,capture_output=True,text=True)
			if("Permission denied" in process.stdout):
				print("[ERR] Permission error while trying to create config file")
			else:
				try:
					self.WriteToConfigFile(Username=Username)
					print("[DEB] Config file created with a basic configuration")
				except PermissionError:
					print("[ERR] Error while creating config file")
	
	def WriteToConfigFile(self,Username):
		with open(f"/home/{Username}/.config/pi_watch/config","w") as op:
			op.write(self.BASIC_CONFIG)
			op.close()
	
	def ReadConfigFile(self, Username="nep"):
		with open(f"/home/{Username}/.config/pi_watch/config","r") as op:
			x = op.readline()
			op.close()
			return x
				


watchout = ["Guild Wars 2","League of Legends","Riot Client"]
killpicom = False
something = ConfigFile()

something.OpenConfigFile()

print(something.compozitor)

print(json.dumps(something.__dict__))

while(0):
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
