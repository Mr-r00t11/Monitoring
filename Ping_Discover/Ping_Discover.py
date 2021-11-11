from pygame import mixer
import datetime
import time
import json
import os

class Ping():
    def __init__(self, ip_1, ip_2, ip_3, ip_4):
        self.ip_1 = ip_1
        self.ip_2 = ip_2
        self.ip_3 = ip_3
        self.ip_4 = ip_4

        self.alive_1 = ''
        self.alive_2 = ''
        self.alive_3 = ''
        self.alive_4 = ''

        self.sound = 0

        self.date_1 = datetime.datetime.now()
        self.date_2 = datetime.datetime.now()
        self.date_3 = datetime.datetime.now()
        self.date_4 = datetime.datetime.now()

        while True:
            self.IP_1()
            self.IP_2()
            self.IP_3()
            self.IP_4()
            self.Create_Json()
            self.Sound_Alert()
            time.sleep(20)

    def IP_1(self):
        self.response_1 = os.popen('ping ' + self.ip_1).read()
        if 'Received = 4' in self.response_1:
            self.alive_1 = 'Up'
            with open('output.txt', 'a') as file_1:
                self.date_1 = datetime.datetime.now()
                file_1.write('[+] ' + self.ip_1 + ' ' + self.alive_1 + ' ' + str(self.date_1) + '\n')
                file_1.close()
                print('[+] ' + self.ip_1 + ' ' +  self.alive_1)
        else:
            with open('output.txt', 'a') as file_1:
                self.date_1 = datetime.datetime.now()
                self.alive_1 = 'Down'
                file_1.write('[-] ' + self.ip_1  + ' ' + self.alive_1 + ' ' + str(self.date_1) + '\n')
                file_1.close()
                print('[-] ' + self.ip_1 + ' ' + self.alive_1)
                self.sound = self.sound + 1
        
    def IP_2(self):
        self.response_2 = os.popen('ping ' + self.ip_2).read()
        if 'Received = 4' in self.response_2:
            self.alive_2 = 'Up'
            with open('output.txt', 'a') as file_2:
                self.date_2 = datetime.datetime.now()
                file_2.write('[+] ' + self.ip_2 + ' ' + self.alive_2 + ' ' + str(self.date_2) + '\n')
                file_2.close()
                print('[+] ' + self.ip_2 + ' ' + self.alive_2)
        else:
            with open('output.txt', 'a') as file_2:
                self.date_2 = datetime.datetime.now()
                self.alive_2 = 'Down'
                file_2.write('[-] ' + self.ip_2  + ' ' + self.alive_2 + ' ' + str(self.date_2) + '\n')
                file_2.close()
                print('[-] ' + self.ip_2 + ' ' + self.alive_2)
                self.sound = self.sound + 1
        
    def IP_3(self):
        self.response_3 = os.popen('ping ' + self.ip_3).read()
        if 'Received = 4' in self.response_3:
            self.alive_3 = 'Up'
            with open('output.txt', 'a') as file_3:
                self.date_3 = datetime.datetime.now()
                file_3.write('[+] ' + self.ip_3 + ' ' + self.alive_3 + ' ' + str(self.date_3) + '\n')
                file_3.close()
                print('[+] ' + self.ip_3 + ' ' + self.alive_3)
        else:
            with open('output.txt', 'a') as file_3:
                self.date_3 = datetime.datetime.now()
                self.alive_3 = 'Down'
                file_3.write('[-] ' + self.ip_3  + ' ' + self.alive_3 + ' ' + str(self.date_3) + '\n')
                file_3.close()
                print('[-] ' + self.ip_3 + ' ' + self.alive_3)
                self.sound = self.sound + 1
        
    def IP_4(self):
        self.response_4 = os.popen('ping ' + self.ip_4).read()
        if 'Received = 4' in self.response_4:
            self.alive_4 = 'Up'
            with open('output.txt', 'a') as file_4:
                self.date_4 = datetime.datetime.now()
                file_4.write('[+] ' + self.ip_4 + ' ' + self.alive_4 + ' ' + str(self.date_4) + '\n')
                file_4.close()
                print('[+] ' + self.ip_4 + ' ' + self.alive_4)
        else:
            with open('output.txt', 'a') as file_4:
                self.date_4 = datetime.datetime.now()
                self.alive_4 = 'Down'
                file_4.write('[-] ' + self.ip_4 + ' ' + self.alive_4 + ' ' + str(self.date_4) + '\n')
                file_4.close()
                print('[-] ' + self.ip_4 + ' ' + self.alive_4)
                self.sound = self.sound + 1
        print("\n")

    def Create_Json(self):
        self.data = {
            'IP_1': self.ip_1,
            'IP_2': self.ip_2,
            'IP_3': self.ip_3,
            'IP_4': self.ip_4,
            'Status_1': self.alive_1,
            'Status_2': self.alive_2,
            'Status_3': self.alive_3,
            'Status_4': self.alive_4
        }

        with open("dicc.json", 'w') as self.json_write:
            self.json_format = json.dumps(self.data, indent=4)
            self.json_write.write(self.json_format)
            self.json_write.close()
        
    def Sound_Alert(self):
        if self.sound >= 1:
            mixer.init()
            mixer.music.load("sound.wav")
            mixer.music.play()
            print(self.sound)
        self.sound = 0

if __name__ == '__main__':
    Ping_Host = Ping(ip_1='148.250.107.71', ip_2='148.250.107.72', ip_3='148.250.108.71', ip_4 = '148.250.108.72')
