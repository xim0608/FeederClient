import serial
import time
import struct


class NanoBoardAG:
    def __init__(self):
        self.valResistanceD = float()
        self.valResistanceC = float()
        self.valResistanceB = float()
        self.valButton = float()
        self.valResistanceA = float()
        self.valLight = float()
        self.valSound = float()
        self.valSlider = float()
        self.is_motor_on = False
        self.motorDirection = 0
        self.motorPower = 100

        self.ser = serial.Serial("/dev/cu.usbserial", 38400, timeout=1)  # macOS sierra
        # self.ser = serial.Serial("/dev/ttyUSB0",38400)  # Linux
        time.sleep(1.8)  # wait fot start...
        self.data = [0]*18

    def set_value(self, data):
        self.valResistanceD = ((data[2] & 0x07) * 128 + data[3]) * 100 / 1023.0
        self.valResistanceC = ((data[4] & 0x07) * 128 + data[5]) * 100 / 1023.0
        self.valResistanceB = ((data[6] & 0x07) * 128 + data[7]) * 100 / 1023.0
        self.valButton = 100 - ((data[8] & 0x07) * 128 + data[9]) * 100 / 1023.0
        self.valResistanceA = ((data[10] & 0x07) * 128 + data[11]) * 100 / 1023.0
        self.valLight = 100 - ((data[12] & 0x07) * 128 + data[13]) * 100 / 1023.0
        self.valSound = ((data[14] & 0x07) * 128 + data[15]) * 100 / 1023.0
        self.valSlider = ((data[16] & 0x07) * 128 + data[17]) * 100 / 1023.0

    def run(self):
        if self.is_motor_on:
            self.send_data()
        else:
            self.ser.write(b'\x00')
        temp = self.ser.read(18)
        self.data = struct.unpack('18B', temp)
        self.set_value(self.data)

    def set_motor_power(self, power):
        self.motorPower = int(power * 1.28)

    def reverse_motor_direction(self):
        self.motorDirection = (self.motorDirection + 1) & 0x1

    def send_data(self):
        self.ser.write((self.motorDirection << 7 | self.motorPower).to_bytes(1, 'big'))


# if __name__ == '__main__':
#     nano = NanoBoardAG()
#     nano.run()
#     print(nano.valSound)
#     time.sleep(2)
#     nano.reverse_motor_direction()
#     nano.set_motor_power(50)
#     nano.is_motor_on = True
#     # nano.reverse_motor_direction()
#     nano.run()
#     time.sleep(3)
#     nano.is_motor_on = False
#     nano.run()
