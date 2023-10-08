#!/bin/bash

#This script requires apt update AND apt list --upgradeable to work without sudo
#This can be done the easiest by adding %{USERNAME} ALL=NOPASSWD: /bin/apt update, /bin/apt list upgradable to the sudoers file

sudo apt update > /dev/null
OUTPUT=$(sudo apt list --upgradable | wc -l)
echo "" $OUTPUT

