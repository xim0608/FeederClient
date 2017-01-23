from NanoBoardAG import NanoBoardAG
from mylib import Lib
from datetime import datetime
import time, sys
from user import User


class Microcom:
    def __init__(self, volume=2):
        print("Welcome to Cat Feeder!!")
        self.micro_com = NanoBoardAG()
        Lib.prints("NanoBoard connected")
        self.volume = volume
        self.micro_com.motorPower = 70
        self.empty_timer = 0
        Lib.prints("Please enter your e-mail and password")
        email = input('E-Mail: ')
        password = input('Password: ')
        self.user = User(email, password)

    def monitoring(self):
        get_sound = True
        self.micro_com.run()
        # check waiting table every 10 seconds
        if int(datetime.utcnow().strftime('%S')) % 10 == 0:
            if self.user.check_waiting():
                get_sound = False
                self.feed()
                self.user.delete_from_waiting()
                time.sleep(5)
                get_sound = True
        # if sound sensor post action
        if self.micro_com.valSound >= 30 and get_sound:
            self.user.post_action()
            time.sleep(30)

        # if self.micro_com.valLight >= 99:
        #     self.send_action()
        #     self.empty_timer

    def feed(self):
        Lib.prints("Feeding..")
        # motor on
        self.micro_com.is_motor_on = True
        self.micro_com.run()
        # motoring 0.5
        time.sleep(0.1)
        # motor off
        self.micro_com.is_motor_on = False
        self.micro_com.run()
        # wait to finish feeding..
        time.sleep(0.2)
        # motor reverse
        self.micro_com.reverse_motor_direction()
        # motor on
        self.micro_com.is_motor_on = True
        self.micro_com.run()
        time.sleep(0.1)
        # motor off
        self.micro_com.is_motor_on = False
        self.micro_com.run()

    def logging(self):
        self.micro_com.run()


if __name__ == '__main__':
    board = Microcom()
    if board.user.login():
        Lib.prints("start logging...")
        try:
            while True:
                board.monitoring()
        except KeyboardInterrupt:
            Lib.prints("Exit")
            sys.exit()





