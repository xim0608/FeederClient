import requests
import time
from mylib import Lib

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.failed_counter = 0
        self.s = requests.Session()
        self.login_time = float()

    def payload(self):
        return {'email': self.email, 'password': self.password}

    def login(self):
        self.s = requests.Session()
        login = self.s.post('https://mysterious-gorge-38499.herokuapp.com/login', data=self.payload())
        if login.status_code == 200:
            Lib.prints("Login succeeded")
            self.login_time = time.time()
            return True
        else:
            Lib.prints("failed to Login")
            self.login()

    def logout(self):
        if time.time() - self.login_time < 300:
            self.s.get('https://mysterious-gorge-38499.herokuapp.com/logout')
            # print("Logout Succeeded")

    def post_action(self):
        Lib.prints("Action!!")
        self.login()
        post = self.s.post('https://mysterious-gorge-38499.herokuapp.com/action/add/')
        if post.status_code == 200:
            Lib.prints("Added Succeeded")
        else:
            Lib.prints("Failed to add action")
            self.failed_counter += 1
            if self.failed_counter < 5:
                self.post_action()
            else:
                Lib.prints("Failed to add")

    def check_waiting(self):
        Lib.prints("Check Server...")
        self.login()
        get = self.s.get('https://mysterious-gorge-38499.herokuapp.com/feed/check/')
        if get.status_code == 302:
            return True
        else:
            time.sleep(1)
            return False


    def delete_from_waiting(self):
        delete = self.s.delete('https://mysterious-gorge-38499.herokuapp.com/feed/delete/')
        Lib.prints('deleted from waiting list')






