monitors=("HDMI-0" "DVI-D-0" "DP-1")
if type "xrandr"; then
  #for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
   for m in ${monitors[@]}; do
     if [[ $m == *"DVI"* ]];
     then
	MONITOR=$m MODULES_LEFT="i3" polybar --reload example &
     else
	MONITOR=$m MODULES_LEFT="i3 xwindow" polybar --reload example &
     fi
     echo $MODULES_LEFT
     sleep 1
  done
else
  polybar --reload example &
fi
