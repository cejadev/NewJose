#!/bin/bash

echo -n "Print message?"

valid=0

while
[ $valid == 0 ]
do 
	read ans
	case $ans in
	yes|YES|y|Y) echo Will print the message 
		     echo The Message 
		     valid=1
		     ;;
	[nN][oO]	)echo will NOT print the message
	*		)echo Yes Or No of some form please ;;
	esac 							
done
