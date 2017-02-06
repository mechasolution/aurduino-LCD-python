import serial
import time
import datetime
import os

ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 9600
ser.open()

count = 0

while (True) :
    if(ser.inWaiting() > 0):
        break;

while (True) :
    now = datetime.datetime.now()
    ser.write(str.encode("{:%Y%b%d %H:%M}\r\n".format(now)))
    ser.write(str.encode(os.environ.get('USERNAME') + "\r\n"))
    time.sleep(1);
