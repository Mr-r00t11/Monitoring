from pygame import mixer
import datetime
import socket
import time
import json

class Sockets_Alive():
    pass

    def __init__(self):
        self.ip_1 = '192.168.100.22'
        self.ip_2 = '192.168.100.22'
        self.ip_3 = '192.168.100.22'

        self.port_1 = 22
        self.port_2 = 22
        self.port_3 = 22

        self.sound = 0

        self.alive_1 = ''
        self.alive_2 = ''
        self.alive_3 = ''

        self.NAC_1 = 'NAC 1'
        self.NAC_2 = 'NAC 2'
        self.NAC_3 = 'NAC 3'

        self.date = datetime.datetime.now()

    def Connect_Port(self):
        self.s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.alive_1 = 'Up'
            self.s1.connect((self.ip_1, self.port_1))
            self.s1.close()
            socket.setdefaulttimeout(10)
            self.file1 = open('output.txt', 'a')
            self.file1.write(str(self.date) + " status: " + str(self.alive_1) + " Appliance: " + self.NAC_1 + '\n')
            self.file1.close()
            print("[+] Port Open")
        except:
            self.alive_1 = 'Down'
            self.file1 = open('output.txt', 'a')
            self.file1.write(str(self.date) + " status: " + str(self.alive_1) + " Appliance: " + self.NAC_1 + '\n')
            self.file1.close()
            print("[-] Port Close")
            self.sound = self.sound + 1
        self.Create_Json()

        try:
            self.alive_2 = 'Up'
            self.s2.connect((self.ip_2, self.port_2))
            self.s2.close()
            socket.setdefaulttimeout(10)
            self.file2 = open('output.txt', 'a')
            self.file2.write(str(self.date) + " status: " + str(self.alive_2) + " Appliance: " + self.NAC_2 + '\n')
            self.file2.close()
            print("[+] Port Open")
        except:
            self.alive_2 = 'Down'
            self.file2 = open('output.txt', 'a')
            self.file2.write(str(self.date) + " status: " + str(self.alive_2) + " Appliance: " + self.NAC_2 + '\n')
            self.file2.close()
            print("[-] Port Close")
            self.sound = self.sound + 1
        self.Create_Json()

        try:
            self.alive_3 = 'Up'
            self.s3.connect((self.ip_3, self.port_3))
            self.s3.close()
            socket.setdefaulttimeout(10)
            self.file3 = open('output.txt', 'a')
            self.file3.write(str(self.date) + " status: " + str(self.alive_3) + " Appliance: " + self.NAC_3 + '\n')
            self.file3.close()
            print("[+] Port Open")
        except:
            self.alive_3 = 'Down'
            self.file3 = open('output.txt', 'a')
            self.file3.write(str(self.date) + " status: " + str(self.alive_3) + " Appliance: " + self.NAC_3 + '\n')
            self.file3.close()
            print("[-] Port Close")
            self.sound = self.sound + 1
        self.Create_Json()
        return 'Port scan completed...'

    def Create_Json(self):
        self.data = {
            'Status_1': self.alive_1,
            'Status_2': self.alive_2,
            'Status_3': self.alive_3
        }

        with open("dicc.json", 'w') as self.json_write:
            self.json_format = json.dumps(self.data, indent=4)
            self.json_write.write(self.json_format)
            self.json_write.close()
            return 'Json file completed...'
        
    def Sound_Alert(self):
        if self.sound >= 1:
            mixer.init()
            mixer.music.load("sound.wav")
            mixer.music.play()
            return self.sound
        self.sound = 0

if __name__ == '__main__':
    Object_Socket = Sockets_Alive()
    while True:
        print(Object_Socket.Connect_Port())
        print(Object_Socket.Create_Json())
        print(Object_Socket.Sound_Alert())
        time.sleep(10)