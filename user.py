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
        # define server address
        self.server_address = 'http://127.0.0.1:5000'
        # https://mysterious-gorge-38499.herokuapp.com

    def payload(self):
        return {'email': self.email, 'password': self.password}

    def login(self):
        self.s = requests.Session()
        login_address = self.server_address + '/login'
        login = self.s.post(login_address, data=self.payload())
        if login.status_code == 200:
            Lib.prints("Login succeeded")
            self.login_time = time.time()
            return True
        else:
            Lib.prints("failed to Login")
            self.login()

    def logout(self):
        if time.time() - self.login_time < 300:
            logout_address = self.server_address + '/logout'
            self.s.get('logout_address')
            # print("Logout Succeeded")

    # if sound sensor
    def post_action(self):
        Lib.prints("Action!!")
        self.login()
        post_action_address = self.server_address + '/action/add'
        post = self.s.post(post_action_address)
        if post.status_code == 200:
            Lib.prints("Added Succeeded")
        else:
            Lib.prints("Failed to add action")
            self.failed_counter += 1
            if self.failed_counter < 5:
                self.post_action()
            else:
                Lib.prints("Failed to add")

    # check waiting table on server
    def check_waiting(self):
        Lib.prints("Check Server...")
        self.login()
        check_waiting_address = self.server_address + '/feed/check/'
        get = self.s.get(check_waiting_address)
        if get.status_code == 302:
            return True
        else:
            time.sleep(1)
            return False

    # delete my user_id from server
    def delete_from_waiting(self):
        delete_address = self.server_address + '/feed/delete/'
        delete = self.s.delete(delete_address)
        Lib.prints('deleted from waiting list')






