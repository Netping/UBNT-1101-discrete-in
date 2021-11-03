#!/usr/bin/python3
import serial
import serial.rs485
import time




def main():
    s = serial.Serial(port='/dev/dkst1101/COM17',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

    s.rs485_mode = serial.rs485.RS485Settings()

    cmd = '$336\r'
    cmd = ''.join(str(ord(c)) for c in cmd)
    x = cmd.encode('ascii')

    s.write(x)
    print(x)
    time.sleep(0.2)
    text = s.readline()
    temp = text.decode('ascii')
    print(temp)

    s.close()

if __name__ == "__main__":
    main()
