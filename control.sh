#!/bin/sh

#sudo python3 monitormode.py
#exit
#sleep 5
#echo "1"
#xdotool key ctrl+c
#echo "HEllo"
#sleep 3
#echo "Bye"

: 'hour=0
min=0
sec=10
       while [ $hour -ge 0 ]; do
                while [ $min -ge 0 ]; do
                        while [ $sec -ge 0 ]; do
                                echo -ne "$hour:$min:$sec\033[0K\r"
                                let "sec=sec-1"
                                sleep 1
                        done
                        sec=59
                        let "min=min-1"
                done
                min=59
                let "hour=hour-1"
        done '

: 'sec=5
	while [ $sec -ge 0 ]; do
		#echo $sec
		sec=$((sec-1))
		sleep 1
		sudo python3 monitormode.py
	done '


sudo python3 mm.py > ssid
cat ssid | tail -18 | grep [0-9a-z] | sort -t: -k2,2r | uniq | sed 's/[ \t]*$//' | sed 's/^[ \t]*//' | awk 'length($0)>21' > sid 
# tail to display only last 18 lines, Grep the lines starting with digits, Sort in reverse order ,AWK used to remove lines with less than 3 characters
echo "Done editing"
#sudo python read.py


