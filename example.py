import serial
import time
import datetime
import os

ser = serial.Serial()
ser.port = 'COM3' #사용하는 포트번호를 입력합니다.
ser.baudrate = 9600
ser.open()

count = 0

while (True) : #아두이노보드의 첫 출력 이후 데이터 전송을 시작합니다.
    if(ser.inWaiting() > 0):
        break;

while (True) :
    #전송하는 줄의 끝마다 \r\n 이 붙어야 합니다.
    now = datetime.datetime.now()
    ser.write(str.encode("{:%Y%b%d %H:%M}\r\n".format(now)))
    ser.write(str.encode(os.environ.get('USERNAME') + "\r\n"))
    time.sleep(1);#1초 간격으로 화면을 갱신합니다.
