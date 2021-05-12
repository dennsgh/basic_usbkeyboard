import time
import struct

ABS_ID=3 #for communication of absoulute coordinates
CLICK_ID=2 #for communication of relative coordinates and clicks
wheel=0 #if wheel shall be used set to 1 and modify code further (communication of abs values), here never used
LMB_ID=1 #LMB, RMB=2
RMB_ID=2

def sendReporter(data):
    print(data)
    with open('/dev/hidg0','wb') as fd:
        fd.write(data)

# If you move to x = 50, y = 100 and your monitor's resolution is 1920 * 1080, your input has to be like this:
# x = 50 * 32767 / 1920 = 853 >>> AS PACKED HID REPORTER
# y = 100 * 32767 / 1080 = 3033 >> AS PACKED HID REPORTER

# Maybe implement resolution changing?
def sendCoordinates(x,y):
    x= int(x*(32767/1920))
    y= int(y*(32767/1080))
    if x>32767: x=32767
    if y>32767: y=32767
    var=struct.pack('<Bhhb',ABS_ID,x,y,0) #pay attention to little endian (<)
    sendReporter(var)


def sendClick(button):
    var=struct.pack('BBbb',CLICK_ID,button,0,0)
    sendReporter(var)
    time.sleep(0.1)
    var=struct.pack('BBbb',CLICK_ID,0,0,0)
    sendReporter(var)
    
# For double click it needs to detect mouse release ('BBbb',CLICK_ID,0,0,0)    
def sendDClick(button):
    sendClick(button)
    sendClick(button)


def main ():
    sendCoordinates(960,540)
    sendDClick(LMB_ID)


if (__name__ == "__main__"):
    main()
