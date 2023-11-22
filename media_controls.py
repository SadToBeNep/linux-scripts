#!/bin/python3

"""Used to execute commands"""
import subprocess
import re

## This script was made to be used with polybar ##
# Requires playerctl to be installed

TITLE_PATTERN = r'xesam:title\s+([^\n]+)'
ARTIST_PATTERN = r'xesam:artist\s+([^\'\[\]]+)'


#### Get the currently playing song ####
returned_data = subprocess.run(['playerctl','metadata'],
                               capture_output=True,text=True,check=False).stdout.split("\n")
try:
    ARTIST = returned_data[3]
    TITLE = returned_data[4]
    MAX_CHARACTERS = 35

    match = re.search(TITLE_PATTERN, TITLE)

    # Check if a match was found
    if match:
        song_title = match.group(1)
        TITLE = song_title.strip()
    else:
        TITLE = "X"



    match = re.search(ARTIST_PATTERN, ARTIST)

    # Check if a match was found
    if match:
        song_artist = match.group(1)
        ARTIST = song_artist.strip()
    else:
        ARTIST = "Y"



    OUTPUT = f"{ARTIST} - {TITLE}"
    if len(OUTPUT) > MAX_CHARACTERS:
        OUTPUT = OUTPUT[0:MAX_CHARACTERS]
    print(OUTPUT)
except IndexError:
    print("-*-")
