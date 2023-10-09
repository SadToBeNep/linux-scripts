#!/bin/python3

## This script was made to be used with polybar ##
# Requires playerctl to be installed

title_pattern = r'xesam:title\s+([^\'\[\]]+)'
artist_pattern = r'xesam:artist\s+([^\'\[\]]+)'




import subprocess,re

#### Get the currently playing song ####
returned_data = subprocess.run(['playerctl','metadata'],capture_output=True,text=True).stdout.split("\n")
ARTIST = returned_data[3]
TITLE = returned_data[1]
MAX_CHARACTERS = 35

match = re.search(title_pattern, TITLE)

# Check if a match was found
if match:
    song_title = match.group(1)
    TITLE = song_title.strip()
else:
    print("No match found.")



match = re.search(artist_pattern, ARTIST)

# Check if a match was found
if match:
    song_artist = match.group(1)
    ARTIST = song_artist.strip()
else:
    print("No match found.")



OUTPUT = f"{ARTIST} - {TITLE}"
if(len(OUTPUT) > MAX_CHARACTERS):
    OUTPUT = OUTPUT[0:MAX_CHARACTERS]
print(OUTPUT)