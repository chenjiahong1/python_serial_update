import time
import serial
import threading


def checksum(data, len):
    i = 0
    sum = 0
    while i < len:
        sum = sum + data[i]
        i = i + 1
    return sum


def read_thread():
    a = [0, 0, 0, 0, 0, 0, 0]
    # mycom.write(bytearray([a[0], a[1]]))
    # mycom.write(bytearray([1, 2, 3]))

    # mycom.write(a[1])
    while 1:
        print("hello")
        a[2] = (1000000 >> 24) & 0xff
        a[3] = (1000000 >> 16) & 0xff
        a[4] = (1000000 >> 8) & 0xff
        a[5] = 1000000 & 0xff

        i = 0
        j = 0
        with open('过级资料.zip', mode='rb') as fd:
            while 1:
                i = i + 1
                if i > 255:
                    j = j + 1
                    i = 0
                time.sleep(1)
                data = fd.read(3)
                a[0] = j
                a[1] = i
                mycom.write(bytearray([a[0], a[1], a[3], a[4], a[5], a[6]]))
                sum = checksum(data, 3)
                mycom.write(data)
                print(sum)
                # mycom.write(str(sum).encode('UTF-8'))


try:
    mycom = serial.Serial("com4", 115200, timeout=50)
    if (mycom.isOpen() == True):
        print("serial is opened")
except Exception as exc:
    print("serial error")


print("Hello, World!")
read_thread()
