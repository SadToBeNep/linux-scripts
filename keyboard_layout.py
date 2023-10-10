#!/bin/python3

## A script made to toggle between different keyboard layouts

### Imports ###
import subprocess
import sys




def toggle_layout():
    ### Get current layout
    returned_data = subprocess.run(['setxkbmap','-query'],capture_output=True,text=True).stdout.split('\n')[-2].split(":")[-1].strip()
    if('us' in returned_data):
        subprocess.run(['setxkbmap','sk'])
    else:
        subprocess.run(['setxkbmap','us'])

def print_layout():
    returned_data = subprocess.run(['setxkbmap','-query'],capture_output=True,text=True).stdout.split('\n')[-2].split(":")[-1].strip()
    print(returned_data)

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        toggle_layout()
    else:
        print_layout()