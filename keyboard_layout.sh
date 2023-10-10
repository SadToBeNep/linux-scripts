#!/bin/bash

layout=$(setxkbmap -query | grep layout | awk '{print substr($0, length($0)-1)}')

if [ "$layout" == "us" ]; then
    setxkbmap sk
else
    setxkbmap us
fi