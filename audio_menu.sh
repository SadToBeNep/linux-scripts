#!/bin/bash

# Function to display the menu
show_menu() {
    clear
    echo "Select an audio output:"
    options=("Speaker" "Headset" "HDMI 1" "HDMI 2" "Quit")
    select choice in "${options[@]}"; do
        case $REPLY in
            1) speaker_function;;
            2) headset_function;;
            3) hdmi1_function;;
            4) hdmi2_function;;
            5) exit;;
            *) echo "Invalid option. Try again.";;
        esac
    done
}

# Function for Speaker
speaker_function() {
    echo "Selected Speaker."
    pactl set-default-sink alsa_output.pci-0000_00_1f.3.analog-stereo
    read -rp "Press Enter to continue..."
}

# Function for Headset
headset_function() {
    echo "Selected Headset."
    pactl set-default-sink alsa_output.usb-Corsair_CORSAIR_VIRTUOSO_Wireless_Gaming_Headset_16adc305000000da-00.analog-stereo
    read -rp "Press Enter to continue..."
}

# Function for HDMI 1
hdmi1_function() {
    echo "Selected HDMI 1."
    pactl set-card-profile alsa_card.pci-0000_01_00.1 output:hdmi-stereo-extra1
    pactl set-default-sink alsa_output.pci-0000_01_00.1.hdmi-stereo-extra1
    read -rp "Press Enter to continue..."
}

# Function for HDMI 2
hdmi2_function() {
    echo "Selected HDMI 2."
    pactl set-card-profile alsa_card.pci-0000_01_00.1 output:hdmi-stereo-extra2
    pactl set-default-sink alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2
    read -rp "Press Enter to continue..."
}

# Check if a choice argument was provided
if [ $# -eq 1 ]; then
    case "$1" in
        "Speaker") speaker_function;;
        "Headset") headset_function;;
        "HDMI1") hdmi1_function;;
        "HDMI2") hdmi2_function;;
        *) echo "Invalid argument. Available options: Speaker, Headset, HDMI1, HDMI2";;
    esac
else
    # Main script
    while true; do
        show_menu
    done
fi
