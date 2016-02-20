#!/bin/bash
chmod 755 Bluetooth.sh

a=10
prevSend=1024

while [ $a -ge 10 ]
sleep 2
do 
sendVal=$(tail -1 /var/lib/cloud9/CAN_BBB/Msg5Data.dat | head -1)
if ([[ "$sendVal" == "$prevSend" ]]) 
then
continue
else
if ([[ "$prevSend" == 1024 ]])
then
continue
else
echo $sendVal >>/dev/rfcomm0
prevSend=$sendVal
fi
fi
done