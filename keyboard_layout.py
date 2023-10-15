#!/bin/python3

## A script made to toggle between different keyboard layouts

### Imports ###
"""Module providing a function printing python version."""
import subprocess
import sys




def toggle_layout():
    """Toggling between given layouts"""

    ### Get current layout
    returned_data = subprocess.run(['setxkbmap','-query'],
                                   capture_output=True,text=True,check=False)
    returned_data = returned_data.stdout.split('\n')[-2].split(":")[-1].strip()
    if 'us' in returned_data:
        subprocess.run(['setxkbmap','sk'],check=False)
    else: subprocess.run(['setxkbmap','us'],check=False)

def print_layout():
    """Just printing out the current layout"""
    returned_data = subprocess.run(['setxkbmap','-query'],
                                   capture_output=True,text=True,check=False)
    returned_data = returned_data.stdout.split('\n')[-2].split(":")[-1].strip()
    print(returned_data)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        toggle_layout()
    else: print_layout()
