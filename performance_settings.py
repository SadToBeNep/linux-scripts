#!/bin/python3
"""Used to execute commands"""
import subprocess
import sys


## This script was made to be used with polybar
POWERSAVE_GLYPH = " 󱙷 "
PERFORMANCE_GLYPH = " 󰲉 "


def read_current_setting():
    """Reads the current CPU gov setting"""
    cpu_speed = subprocess.run(['/home/nep/Scripts/read_cpu_ghz.sh'],
                               capture_output=True,text=True,check=False)

    cpu_speed = cpu_speed.stdout.split("\n")
    average = 0
    count = 0
    for line in cpu_speed:
        if len(line) < 2:
            pass
        else:
            average += float(line.split(":")[-1].strip())
            count+=1
    cpu_speed = int(average/count)/1000
    cpu_speed = f"{cpu_speed:.2f}"

    return_data = subprocess.run(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'],
                                 capture_output=True,text=True,check=False)

    if "powersave" in return_data.stdout:
        print(f"{POWERSAVE_GLYPH} {cpu_speed} GHz")
    else: print(f"{PERFORMANCE_GLYPH} {cpu_speed} GHz")

def change_to_another_mode():
    """Changes the mode to another"""
    return_data = subprocess.run(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'],
                                 capture_output=True,text=True,check=False)
    if "powersave" in return_data.stdout:
        subprocess.run(['sudo','to_performance'],check=False)
    else:subprocess.run(['sudo','to_powersave'],check=False)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        change_to_another_mode()
    else: read_current_setting()
    