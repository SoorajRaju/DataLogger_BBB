import time
import datetime 
import os
import can
import subprocess

class canlog():
    def __init__(self, file):
        self.file = open(file, 'w', 0)

    def filewrite(self, what):
        self.file.write(what)
        self.file.flush()
    
    def __getattr__(self, attr):
       return getattr(self.file, attr)

timestr = time.strftime("%Y%m%d_%H%M")

myfilename = "Msg565Data_"+timestr+".dat"  #filename to store data
IntFileName= "Msg565Data.dat"
bus = can.interface.Bus('vcan0', bustype='socketcan_ctypes')
#bus = can.interface.Bus('can0', bustype='socketcan_ctypes')
fileinit=0
CAN_Data_Internal=[]

print "Start at "+str(datetime.datetime.now())

while 1:
    msg= bus.recv(25)
    if msg is not None:
        CAN_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        if fileinit==0:
            file=canlog(myfilename);
            IntFile=canlog(IntFileName);
            file.filewrite('#CAN LOGGING '+ 'at '+ str(CAN_time))
            fileinit=1
            
        #print "Recived"    
        #CAN ID formating
        CAN_id=str(hex(msg.arbitration_id))[0:-1]

        if CAN_id=="0x0aabbccdd":
            data=0
            length=int(msg.dlc)
            for data in range(length):
                CAN_Data_Internal.append(hex(msg.data[data]).decode("utf-8")[2:])
                
            file.filewrite('\n'+str(CAN_time)+","+str(CAN_id)+",")
            IntFile.filewrite(str(CAN_time)+","+str(CAN_id)+",")
            
            for item in CAN_Data_Internal:
                file.filewrite("%s," % item)
                IntFile.filewrite("%s," % item)
            IntFile.filewrite('\n') 
            #for data in range(length):
            #    print CAN_Data_Internal[data]
            print msg
            CAN_Data_Internal[:]=[]
        else:
            print "error"
            print msg
            
    if msg is None:
        break
print "END at "+str(datetime.datetime.now())
