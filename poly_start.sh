monitors=("HDMI-0" "DVI-D-0" "DP-1")
if type "xrandr"; then
  #for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
   for m in ${monitors[@]}; do     
     MONITOR=$m polybar --reload example &
     sleep 1
  done
else
  polybar --reload example &
fi
