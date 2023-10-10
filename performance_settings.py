#!/bin/python3

## This script was made to be used with polybar
POWERSAVE_GLYPH = " 󱙷 "
PERFORMANCE_GLYPH = " 󰲉 "
import subprocess,sys

def read_current_setting():
    
    return_data = subprocess.run(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'], capture_output=True,text=True)
    if("powersave" in return_data.stdout):
        print(POWERSAVE_GLYPH)
    else:
        print(PERFORMANCE_GLYPH)
    

def change_to_another_mode():
    return_data = subprocess.run(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'], capture_output=True,text=True)
    if("powersave" in return_data.stdout):
        subprocess.run(['sudo','to_performance'])
        
    else:
        subprocess.run(['sudo','to_powersave'])

if(__name__ == "__main__"):
    if(len(sys.argv) == 2):
        change_to_another_mode()
    else:
        read_current_setting()
    