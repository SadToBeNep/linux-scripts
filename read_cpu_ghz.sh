#!/bin/bash
mpstat -P ALL 1 1 | awk '/Average:/ {avg+=$NF; count++} END {printf "%.2f GHz", avg/count/100}'