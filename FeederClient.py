from NanoBoardAG import NanoBoardAG
from mylib import Lib
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
        email = input('E-mail:')
        password = input('Password:')
        self.user = User(email, password)

    def monitoring(self):
        self.micro_com.run()
        if self.micro_com.valSound >= 30:
            self.user.post_action()
            time.sleep(30)
        # if self.micro_com.valLight >= 99:
        #     self.send_action()
        #     self.empty_timer

    def feed(self):
        self.micro_com.is_motor_on = True
        time.sleep(self.volume)
        self.micro_com.is_motor_on = False

    def logging(self):
        self.micro_com.run()

    # type 0 = sound
    # @staticmethod
    # def send_action():
    #     user.post_action()





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





