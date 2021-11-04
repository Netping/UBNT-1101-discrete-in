import serial
import serial.rs485
import time
import binascii




class DISCRETE_IN:
    deviceAddr = 1
    ser = None

    def __init__(self, channel):
        if not DISCRETE_IN.ser:
            DISCRETE_IN.ser = serial.Serial(port='/dev/dkst1101/COM17',
                                        baudrate=9600,
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        bytesize=serial.EIGHTBITS,
                                        timeout=1)

            DISCRETE_IN.ser.rs485_mode = serial.rs485.RS485Settings()
            
        self.__channel = 0
        self.__outmap = ''

        if channel.upper() == 'IN1':
            self.__channel = 1
        elif channel.upper() == 'IN2':
            self.__channel = 2
        elif channel.upper() == 'IN3':
            self.__channel = 3
        elif channel.upper() == 'IN4':
            self.__channel = 4
        elif channel.upper() == 'IN5':
            self.__channel = 5
        elif channel.upper() == 'IN6':
            self.__channel = 6
        elif channel.upper() == 'IN7':
            self.__channel = 7
        elif channel.upper() == 'IN8':
            self.__channel = 8
        else
            print('Error: Bad channel name')

    def value(self):
        if self.__outmap[self.__channel - 1] == '1':
            return True

        return False

    def __request(self):
        cmd = '$'+ format(DISCRETE_IN.deviceAddr, '02X') + '6\r'
        cmd = ''.join(str(ord(c)) for c in cmd)
        x = cmd.encode('ascii')

        s.write(x)
        print(x)
        time.sleep(0.2)
        text = s.readline()
        temp = text.decode('ascii')
        temp = temp[1:-5]

        #fill outmap
        self.__outmap = binascii.unhexlify(temp)

    def __del__(self):
        if self.__serial:
            self.__serial.close()
