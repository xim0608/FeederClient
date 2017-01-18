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
        self.empty_timer = 0
        Lib.prints("Please enter your e-mail and password")
        email = input('E-Mail: ')
        password = input('Password: ')
        self.user = User(email, password)

    def monitoring(self):
        self.micro_com.run()
        if self.micro_com.valSound >= 30:
            self.user.post_action()
            time.sleep(30)
        if int(datetime.utcnow().strftime('%S')) % 20 == 0:
            if self.user.check_waiting():
                self.feed()
                self.user.delete_from_waiting()
        # if self.micro_com.valLight >= 99:
        #     self.send_action()
        #     self.empty_timer

    def feed(self):
        Lib.prints("Feeding..")
        self.micro_com.is_motor_on = True
        self.micro_com.run()
        time.sleep(self.volume)
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





