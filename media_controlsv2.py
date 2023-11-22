#!/bin/python
import subprocess


def getArtist():
	return subprocess.run(["playerctl","metadata","artist"],check=False,capture_output=True,text=True).stdout.strip()

def getTitle():
	return subprocess.run(["playerctl","metadata","title"],check=False,capture_output=True,text=True).stdout.strip()




MAX_LEN = 35
TITLE = getTitle()
ARTIST = getArtist()

OUTPUT = f"{ARTIST} - {TITLE}"
print(OUTPUT[:MAX_LEN])
