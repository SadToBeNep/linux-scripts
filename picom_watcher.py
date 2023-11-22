#!/usr/bin/python

import json
import subprocess
from time import sleep
from os import mkdir,path
import psutil

class ConfigFile():
	BASIC_CONFIG = '{"watchout_list": ["Guild Wars 2", "League of Legends", "Riot Client"], "sleep_time": 15, "compozitor": "picom", "config_location": "~/.config/pi_watch/config"}'
	NO_REC = False

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
			if(self.NO_REC == False):
				print(self.NO_REC)
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
			self.NO_REC = True
			return x
				


def is_process_running(process_name):
	for process in psutil.process_iter(['pid', 'name']):
		#print(process.info['name'])
		if process.info['name'] == process_name:
	            return True
	return False

def kill_process(process_name):
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                pid = process.info['pid']
                subprocess.run(['kill', str(pid)])
                print(f"Killed process: {process_name} (PID: {pid})")
    except Exception as e:
        print(f"Error while killing process {process_name}: {e}")

# Replace with the actual names of the processes you're looking for
process_names_to_check = ["Gw2-64.exe", "League of Legends", "Riot Client"]
picom_process_name = "picom"

while(1):
	# Check if any of the specified processes are running
	for process_name in process_names_to_check:
		if is_process_running(process_name):
			print(f"Process {process_name} is running.")
			# If any of the specified processes are running, kill picom
			kill_process(picom_process_name)
			break
		else:
			print(f"Process {process_name} is not running.")

	# If none of the specified processes are running, check if picom is running
	if not any(is_process_running(process_name) for process_name in process_names_to_check):
		if not is_process_running(picom_process_name):
			# If picom is not running, start picom
			subprocess.Popen(['nohup','picom'])
			print("Started picom.")
		else:
			print("picom is already running.")
	else:
		print("picom not started, as at least one of the specified processes is running.")

	print("Script execution completed.")
	sleep(10)
