from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from pygame import mixer
import paramiko
import binascii
import datetime
import getpass
import json
import time
import os

class SSH():
    pass
    def __init__(self, user_1, password_1, user_2, password_2, user_3, password_3, user_4, password_4, user_5, password_5, user_6, password_6, user_7, password_7, user_8, password_8, user_9, password_9, user_10, password_10, user_11, password_11, user_12, password_12, user_13, password_13, user_14, password_14, user_15, password_15):

        self.user_1 = user_1
        self.password_1 = password_1
        self.user_2 = user_2
        self.password_2 = password_2
        self.user_3 = user_3
        self.password_3 = password_3
        self.user_4 = user_4
        self.password_4 = password_4
        self.user_5 = user_5
        self.password_5 = password_5
        self.user_6 = user_6
        self.password_6 = password_6
        self.user_7 = user_7
        self.password_7 = password_7
        self.user_8 = user_8
        self.password_8 = password_8
        self.user_9 = user_9
        self.password_9 = password_9
        self.user_10 = user_10
        self.password_10 = password_10
        self.user_11 = user_11
        self.password_11 = password_11
        self.user_12 = user_12
        self.password_12 = password_12
        self.user_13 = user_13
        self.password_13 = password_13
        self.user_14 = user_14
        self.password_14 = password_14
        self.user_15 = user_15
        self.password_15 = password_15

        self.sound = 0

        self.date_1 = datetime.datetime.now()
        self.alive_1 = ''
        self.appliance_1 = 'ADO1'
        self.output_1 = ''

        self.date_2 = datetime.datetime.now()
        self.alive_2 = ''
        self.appliance_2 = 'ADO2'
        self.output_2 = ''

        self.date_3 = datetime.datetime.now()
        self.alive_3 = ''
        self.appliance_3 = 'ADO3'
        self.output_3 = ''

        self.date_4 = datetime.datetime.now()
        self.alive_4 = ''
        self.appliance_4 = 'ADO4'
        self.output_4 = ''

        self.date_5 = datetime.datetime.now()
        self.alive_5 = ''
        self.appliance_5 = 'ADO5'
        self.output_5 = ''

        self.date_6 = datetime.datetime.now()
        self.alive_6 = ''
        self.appliance_6 = 'ADO6'
        self.output_6 = ''

        self.date_7 = datetime.datetime.now()
        self.alive_7 = ''
        self.appliance_7 = 'ADO7'
        self.output_7 = ''

        self.date_8 = datetime.datetime.now()
        self.alive_8 = ''
        self.appliance_8 = 'ADO8'
        self.output_8 = ''

        self.date_9 = datetime.datetime.now()
        self.alive_9 = ''
        self.appliance_9 = 'ADO9'
        self.output_9 = ''

        self.date_10 = datetime.datetime.now()
        self.alive_10 = ''
        self.appliance_10 = 'ADO10'
        self.output_10 = ''

        self.date_11 = datetime.datetime.now()
        self.alive_11 = ''
        self.appliance_11 = 'ADO11'
        self.output_11 = ''

        self.date_12 = datetime.datetime.now()
        self.alive_12 = ''
        self.appliance_12 = 'ADO12'
        self.output_12 = ''

        self.date_13 = datetime.datetime.now()
        self.alive_13 = ''
        self.appliance_13 = 'ADO13'
        self.output_13 = ''

        self.date_14 = datetime.datetime.now()
        self.alive_14 = ''
        self.appliance_14 = 'ADO14'
        self.output_14 = ''

        self.date_15 = datetime.datetime.now()
        self.alive_15 = ''
        self.appliance_15 = 'ADO15'
        self.output_15 = ''

        self.keyPair = RSA.generate(1024)
        self.pubKey = self.keyPair.publickey()
        self.pubKeyPEM = self.pubKey.exportKey()
        self.privKeyPEM = self.keyPair.exportKey()
        
        while True:
            self.Commands_1()
            self.Commands_2()
            self.Commands_3()
            self.Commands_4()
            self.Commands_5()
            self.Commands_6()
            self.Commands_7()
            self.Commands_8()
            self.Commands_9()
            self.Commands_10()
            self.Commands_11()
            self.Commands_12()
            self.Commands_13()
            self.Commands_14()
            self.Commands_15()
            self.Create_Json()
            self.Sound_Alert()
            time.sleep(20)

    def Encrypt_1(self):
        self.encryptor_1 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_1 = self.encryptor_1.encrypt(self.password_1)
        return "Encrypted:", binascii.hexlify(self.encrypted_1)

    def Decrypt_1(self):
        self.Encrypt_1()
        self.decryptor_1 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_1 = self.decryptor_1.decrypt(self.encrypted_1)
        self.decrypted_ssh_1 = self.decrypted_1.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_1

    def Encrypt_2(self):
        self.encryptor_2 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_2 = self.encryptor_2.encrypt(self.password_2)
        return "Encrypted:", binascii.hexlify(self.encrypted_2)
        pass

    def Decrypt_2(self):
        self.Encrypt_2()
        self.decryptor_2 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_2 = self.decryptor_2.decrypt(self.encrypted_2)
        self.decrypted_ssh_2 = self.decrypted_2.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_2
        pass

    def Encrypt_3(self):
        self.encryptor_3 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_3 = self.encryptor_3.encrypt(self.password_3)
        return "Encrypted:", binascii.hexlify(self.encrypted_3)

    def Decrypt_3(self):
        self.Encrypt_3()
        self.decryptor_3 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_3 = self.decryptor_3.decrypt(self.encrypted_3)
        self.decrypted_ssh_3 = self.decrypted_3.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_3

    def Encrypt_4(self):
        self.encryptor_4 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_4 = self.encryptor_4.encrypt(self.password_4)
        return "Encrypted:", binascii.hexlify(self.encrypted_4)

    def Decrypt_4(self):
        self.Encrypt_4()
        self.decryptor_4 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_4 = self.decryptor_4.decrypt(self.encrypted_4)
        self.decrypted_ssh_4 = self.decrypted_4.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_4

    def Encrypt_5(self):
        self.encryptor_5 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_5 = self.encryptor_5.encrypt(self.password_5)
        return "Encrypted:", binascii.hexlify(self.encrypted_5)

    def Decrypt_5(self):
        self.Encrypt_5()
        self.decryptor_5 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_5 = self.decryptor_5.decrypt(self.encrypted_5)
        self.decrypted_ssh_5 = self.decrypted_5.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_5

    def Encrypt_6(self):
        self.encryptor_6 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_6 = self.encryptor_6.encrypt(self.password_6)
        return "Encrypted:", binascii.hexlify(self.encrypted_6)

    def Decrypt_6(self):
        self.Encrypt_6()
        self.decryptor_6 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_6 = self.decryptor_6.decrypt(self.encrypted_6)
        self.decrypted_ssh_6 = self.decrypted_6.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_6

    def Encrypt_7(self):
        self.encryptor_7 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_7 = self.encryptor_7.encrypt(self.password_7)
        return "Encrypted:", binascii.hexlify(self.encrypted_7)

    def Decrypt_7(self):
        self.Encrypt_7()
        self.decryptor_7 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_7 = self.decryptor_7.decrypt(self.encrypted_7)
        self.decrypted_ssh_7 = self.decrypted_7.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_7

    def Encrypt_8(self):
        self.encryptor_8 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_8 = self.encryptor_8.encrypt(self.password_8)
        return "Encrypted:", binascii.hexlify(self.encrypted_8)

    def Decrypt_8(self):
        self.Encrypt_8()
        self.decryptor_8 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_8 = self.decryptor_8.decrypt(self.encrypted_8)
        self.decrypted_ssh_8 = self.decrypted_8.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_8

    def Encrypt_9(self):
        self.encryptor_9 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_9 = self.encryptor_9.encrypt(self.password_9)
        return "Encrypted:", binascii.hexlify(self.encrypted_9)

    def Decrypt_9(self):
        self.Encrypt_9()
        self.decryptor_9 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_9 = self.decryptor_9.decrypt(self.encrypted_9)
        self.decrypted_ssh_9 = self.decrypted_9.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_9

    def Encrypt_10(self):
        self.encryptor_10 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_10 = self.encryptor_10.encrypt(self.password_10)
        return "Encrypted:", binascii.hexlify(self.encrypted_10)

    def Decrypt_10(self):
        self.Encrypt_10()
        self.decryptor_10 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_10 = self.decryptor_10.decrypt(self.encrypted_10)
        self.decrypted_ssh_10 = self.decrypted_10.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_10

    def Encrypt_11(self):
        self.encryptor_11 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_11 = self.encryptor_11.encrypt(self.password_11)
        return "Encrypted:", binascii.hexlify(self.encrypted_11)

    def Decrypt_11(self):
        self.Encrypt_11()
        self.decryptor_11 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_11 = self.decryptor_11.decrypt(self.encrypted_11)
        self.decrypted_ssh_11 = self.decrypted_11.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_11

    def Encrypt_12(self):
        self.encryptor_12 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_12 = self.encryptor_12.encrypt(self.password_12)
        return "Encrypted:", binascii.hexlify(self.encrypted_12)

    def Decrypt_12(self):
        self.Encrypt_12()
        self.decryptor_12 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_12 = self.decryptor_12.decrypt(self.encrypted_12)
        self.decrypted_ssh_12 = self.decrypted_12.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_12

    def Encrypt_13(self):
        self.encryptor_13 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_13 = self.encryptor_13.encrypt(self.password_13)
        return "Encrypted:", binascii.hexlify(self.encrypted_13)

    def Decrypt_13(self):
        self.Encrypt_13()
        self.decryptor_13 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_13 = self.decryptor_13.decrypt(self.encrypted_13)
        self.decrypted_ssh_13 = self.decrypted_13.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_13

    def Encrypt_14(self):
        self.encryptor_14 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_14 = self.encryptor_14.encrypt(self.password_14)
        return "Encrypted:", binascii.hexlify(self.encrypted_14)

    def Decrypt_14(self):
        self.Encrypt_14()
        self.decryptor_14 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_14 = self.decryptor_14.decrypt(self.encrypted_14)
        self.decrypted_ssh_14 = self.decrypted_14.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_14

    def Encrypt_15(self):
        self.encryptor_15 = PKCS1_OAEP.new(self.pubKey)
        self.encrypted_15 = self.encryptor_15.encrypt(self.password_15)
        return "Encrypted:", binascii.hexlify(self.encrypted_15)

    def Decrypt_15(self):
        self.Encrypt_15()
        self.decryptor_15 = PKCS1_OAEP.new(self.keyPair)
        self.decrypted_15 = self.decryptor_15.decrypt(self.encrypted_15)
        self.decrypted_ssh_15 = self.decrypted_15.decode('utf-8')
        return 'Decrypted:', self.decrypted_ssh_15

    def Commands_1(self):
        self.Encrypt_1()
        self.Decrypt_1()
        try:
            self.list_1 = []
            self.alive_1 = 'Up'
            self.ssh_1 = paramiko.SSHClient()
            self.ssh_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_1.connect('192.168.100.23', port=22, username=self.user_1, password=self.decrypted_ssh_1)
            self.stdin_1, self.stdout_1, self.stderr_1 = self.ssh_1.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_1 = self.stdout_1.read().decode()
            if self.output_1:
                self.date_1 = datetime.datetime.now()
                self.file_1 = open('log_status_ssh.txt', 'a')
                self.file_1.write(str(self.date_1) + " status: " + str(self.alive_1) + " Appliance: " + "AD01 " + 'SSH: ' + str(self.output_1))
                self.file_1.close()
                print("1")
                pass
            pass
        except:
            self.alive_1 = 'Down'
            self.date_1 = datetime.datetime.now()
            self.file_1 = open('log_status_ssh.txt', 'a')
            self.file_1.write(str(self.date_1) + " status: " + str(self.alive_1) + " Appliance: " + "AD01 " + "\n")
            self.file_1.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_2(self):
        self.Encrypt_2()
        self.Decrypt_2()
        try:
            self.list_2 = []
            self.alive_2 = 'Up'
            self.ssh_2 = paramiko.SSHClient()
            self.ssh_2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_2.connect('192.168.100.23', port=22, username=self.user_2, password=self.decrypted_ssh_2)
            self.stdin_2, self.stdout_2, self.stderr_2 = self.ssh_2.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_2 = self.stdout_2.read().decode()
            if self.output_2:
                self.date_2 = datetime.datetime.now()
                self.file_2 = open('log_status_ssh.txt', 'a')
                self.file_2.write(str(self.date_2) + " status: " + str(self.alive_2) + " Appliance: " + "AD02 " + 'SSH: ' + str(self.output_2))
                self.file_2.close()
                print("2")
                pass
            pass
        except:
            self.alive_2 = 'Down'
            self.date_2 = datetime.datetime.now()
            self.file_2 = open('log_status_ssh.txt', 'a')
            self.file_2.write(str(self.date_2) + " status: " + str(self.alive_2) + " Appliance: " + "AD02 " + "\n")
            self.file_2.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_3(self):
        self.Encrypt_3()
        self.Decrypt_3()
        try:
            self.list_3 = []
            self.alive_3 = 'Up'
            self.ssh_3 = paramiko.SSHClient()
            self.ssh_3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_3.connect('192.168.100.23', port=22, username=self.user_3, password=self.decrypted_ssh_3)
            self.stdin_3, self.stdout_3, self.stderr_3 = self.ssh_3.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_3 = self.stdout_3.read().decode()
            if self.output_3:
                self.date_3 = datetime.datetime.now()
                self.file_3 = open('log_status_ssh.txt', 'a')
                self.file_3.write(str(self.date_3) + " status: " + str(self.alive_3) + " Appliance: " + str(self.appliance_3) + ' SSH: ' + str(self.output_3))
                self.file_3.close()
                print("3")
                pass
            pass
        except:
            self.alive_3 = 'Down'
            self.date_3 = datetime.datetime.now()
            self.file_3 = open('log_status_ssh.txt', 'a')
            self.file_3.write(str(self.date_3) + " status: " + str(self.alive_3) + " Appliance: " + str(self.appliance_3) + "\n")
            self.file_3.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_4(self):
        self.Encrypt_4()
        self.Decrypt_4()
        try:
            self.list_4 = []
            self.alive_4 = 'Up'
            self.ssh_4 = paramiko.SSHClient()
            self.ssh_4.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_4.connect('192.168.100.23', port=22, username=self.user_4, password=self.decrypted_ssh_4)
            self.stdin_4, self.stdout_4, self.stderr_4 = self.ssh_4.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_4 = self.stdout_4.read().decode()
            if self.output_4:
                self.date_4 = datetime.datetime.now()
                self.file_4 = open('log_status_ssh.txt', 'a')
                self.file_4.write(str(self.date_4) + " status: " + str(self.alive_4) + " Appliance: " + str(self.appliance_4) + ' SSH: ' + str(self.output_4))
                self.file_4.close()
                print("4")
                pass
            pass
        except:
            self.alive_4 = 'Down'
            self.date_4 = datetime.datetime.now()
            self.file_4 = open('log_status_ssh.txt', 'a')
            self.file_4.write(str(self.date_4) + " status: " + str(self.alive_4) + " Appliance: " + str(self.appliance_4) + "\n")
            self.file_4.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_5(self):
        self.Encrypt_5()
        self.Decrypt_5()
        try:
            self.list_5 = []
            self.alive_5 = 'Up'
            self.ssh_5 = paramiko.SSHClient()
            self.ssh_5.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_5.connect('192.168.100.23', port=22, username=self.user_5, password=self.decrypted_ssh_5)
            self.stdin_5, self.stdout_5, self.stderr_5 = self.ssh_5.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_5 = self.stdout_5.read().decode()
            if self.output_5:
                self.date_5 = datetime.datetime.now()
                self.file_5 = open('log_status_ssh.txt', 'a')
                self.file_5.write(str(self.date_5) + " status: " + str(self.alive_5) + " Appliance: " + str(self.appliance_5) + ' SSH: ' + str(self.output_5))
                self.file_5.close()
                print("5")
                pass
            pass
        except:
            self.alive_5 = 'Down'
            self.date_5 = datetime.datetime.now()
            self.file_5 = open('log_status_ssh.txt', 'a')
            self.file_5.write(str(self.date_5) + " status: " + str(self.alive_5) + " Appliance: " + str(self.appliance_5) + "\n")
            self.file_5.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_6(self):
        self.Encrypt_6()
        self.Decrypt_6()
        try:
            self.list_6 = []
            self.alive_6 = 'Up'
            self.ssh_6 = paramiko.SSHClient()
            self.ssh_6.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_6.connect('192.168.100.23', port=22, username=self.user_6, password=self.decrypted_ssh_6)
            self.stdin_6, self.stdout_6, self.stderr_6 = self.ssh_6.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_6 = self.stdout_6.read().decode()
            if self.output_6:
                self.date_6 = datetime.datetime.now()
                self.file_6 = open('log_status_ssh.txt', 'a')
                self.file_6.write(str(self.date_6) + " status: " + str(self.alive_6) + " Appliance: " + str(self.appliance_6) + ' SSH: ' + str(self.output_6))
                self.file_6.close()
                print("6")
                pass
            pass
        except:
            self.alive_6 = 'Down'
            self.date_6 = datetime.datetime.now()
            self.file_6 = open('log_status_ssh.txt', 'a')
            self.file_6.write(str(self.date_6) + " status: " + str(self.alive_6) + " Appliance: " + str(self.appliance_6) + "\n")
            self.file_6.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_7(self):
        self.Encrypt_7()
        self.Decrypt_7()
        try:
            self.list_7 = []
            self.alive_7 = 'Up'
            self.ssh_7 = paramiko.SSHClient()
            self.ssh_7.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_7.connect('192.168.100.23', port=22, username=self.user_7, password=self.decrypted_ssh_7)
            self.stdin_7, self.stdout_7, self.stderr_7 = self.ssh_7.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_7 = self.stdout_7.read().decode()
            if self.output_7:
                self.date_7 = datetime.datetime.now()
                self.file_7 = open('log_status_ssh.txt', 'a')
                self.file_7.write(str(self.date_7) + " status: " + str(self.alive_7) + " Appliance: " + str(self.appliance_7) + ' SSH: ' + str(self.output_7))
                self.file_7.close()
                print("7")
                pass
            pass
        except:
            self.alive_7 = 'Down'
            self.date_7 = datetime.datetime.now()
            self.file_7 = open('log_status_ssh.txt', 'a')
            self.file_7.write(str(self.date_7) + " status: " + str(self.alive_7) + " Appliance: " + str(self.appliance_7) + "\n")
            self.file_7.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_8(self):
        self.Encrypt_8()
        self.Decrypt_8()
        try:
            self.list_8 = []
            self.alive_8 = 'Up'
            self.ssh_8 = paramiko.SSHClient()
            self.ssh_8.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_8.connect('192.168.100.23', port=22, username=self.user_8, password=self.decrypted_ssh_8)
            self.stdin_8, self.stdout_8, self.stderr_8 = self.ssh_8.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_8 = self.stdout_8.read().decode()
            if self.output_8:
                self.date_8 = datetime.datetime.now()
                self.file_8 = open('log_status_ssh.txt', 'a')
                self.file_8.write(str(self.date_8) + " status: " + str(self.alive_8) + " Appliance: " + str(self.appliance_8) + ' SSH: ' + str(self.output_8))
                self.file_8.close()
                print("8")
                pass
            pass
        except:
            self.alive_8 = 'Down'
            self.date_8 = datetime.datetime.now()
            self.file_8 = open('log_status_ssh.txt', 'a')
            self.file_8.write(str(self.date_8) + " status: " + str(self.alive_8) + " Appliance: " + str(self.appliance_8) + "\n")
            self.file_8.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_9(self):
        self.Encrypt_9()
        self.Decrypt_9()
        try:
            self.list_9 = []
            self.alive_9 = 'Up'
            self.ssh_9 = paramiko.SSHClient()
            self.ssh_9.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_9.connect('192.168.100.23', port=22, username=self.user_9, password=self.decrypted_ssh_9)
            self.stdin_9, self.stdout_9, self.stderr_9 = self.ssh_9.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_9 = self.stdout_9.read().decode()
            if self.output_9:
                self.date_9 = datetime.datetime.now()
                self.file_9 = open('log_status_ssh.txt', 'a')
                self.file_9.write(str(self.date_9) + " status: " + str(self.alive_9) + " Appliance: " + str(self.appliance_9) + ' SSH: ' + str(self.output_9))
                self.file_9.close()
                print("9")
                pass
            pass
        except:
            self.alive_9 = 'Down'
            self.date_9 = datetime.datetime.now()
            self.file_9 = open('log_status_ssh.txt', 'a')
            self.file_9.write(str(self.date_9) + " status: " + str(self.alive_9) + " Appliance: " + str(self.appliance_9) + "\n")
            self.file_9.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_10(self):
        self.Encrypt_10()
        self.Decrypt_10()
        try:
            self.list_10 = []
            self.alive_10 = 'Up'
            self.ssh_10 = paramiko.SSHClient()
            self.ssh_10.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_10.connect('192.168.100.23', port=22, username=self.user_10, password=self.decrypted_ssh_10)
            self.stdin_10, self.stdout_10, self.stderr_10 = self.ssh_10.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_10 = self.stdout_10.read().decode()
            if self.output_10:
                self.date_10 = datetime.datetime.now()
                self.file_10 = open('log_status_ssh.txt', 'a')
                self.file_10.write(str(self.date_10) + " status: " + str(self.alive_10) + " Appliance: " + str(self.appliance_10) + ' SSH: ' + str(self.output_10))
                self.file_10.close()
                self.sound = self.sound + 1
                print("10")
                pass
            pass
        except:
            self.alive_10 = 'Down'
            self.date_10 = datetime.datetime.now()
            self.file_10 = open('log_status_ssh.txt', 'a')
            self.file_10.write(str(self.date_10) + " status: " + str(self.alive_10) + " Appliance: " + str(self.appliance_10) + "\n")
            self.file_10.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_11(self):
        self.Encrypt_11()
        self.Decrypt_11()
        try:
            self.list_11 = []
            self.alive_11 = 'Up'
            self.ssh_11 = paramiko.SSHClient()
            self.ssh_11.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_11.connect('192.168.100.23', port=22, username=self.user_11, password=self.decrypted_ssh_11)
            self.stdin_11, self.stdout_11, self.stderr_11 = self.ssh_11.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_11 = self.stdout_11.read().decode()
            if self.output_11:
                self.date_11 = datetime.datetime.now()
                self.file_11 = open('log_status_ssh.txt', 'a')
                self.file_11.write(str(self.date_11) + " status: " + str(self.alive_11) + " Appliance: " + str(self.appliance_11) + ' SSH: ' + str(self.output_11))
                self.file_11.close()
                print("11")
                pass
            pass
        except:
            self.alive_11 = 'Down'
            self.date_11 = datetime.datetime.now()
            self.file_11 = open('log_status_ssh.txt', 'a')
            self.file_11.write(str(self.date_11) + " status: " + str(self.alive_11) + " Appliance: " + str(self.appliance_11) + "\n")
            self.file_11.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_12(self):
        self.Encrypt_12()
        self.Decrypt_12()
        try:
            self.list_12 = []
            self.alive_12 = 'Up'
            self.ssh_12 = paramiko.SSHClient()
            self.ssh_12.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_12.connect('192.168.100.23', port=22, username=self.user_12, password=self.decrypted_ssh_12)
            self.stdin_12, self.stdout_12, self.stderr_12 = self.ssh_12.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_12 = self.stdout_12.read().decode()
            if self.output_12:
                self.date_12 = datetime.datetime.now()
                self.file_12 = open('log_status_ssh.txt', 'a')
                self.file_12.write(str(self.date_12) + " status: " + str(self.alive_12) + " Appliance: " + str(self.appliance_12) + ' SSH: ' + str(self.output_12))
                self.file_12.close()
                print("12")
                pass
            pass
        except:
            self.alive_12 = 'Down'
            self.date_12 = datetime.datetime.now()
            self.file_12 = open('log_status_ssh.txt', 'a')
            self.file_12.write(str(self.date_12) + " status: " + str(self.alive_12) + " Appliance: " + str(self.appliance_12) + "\n")
            self.file_12.close()
            self.sound = self.sound + 1
        self.Create_Json()
        
    def Commands_13(self):
        self.Encrypt_13()
        self.Decrypt_13()
        try:
            self.list_13 = []
            self.alive_13 = 'Up'
            self.ssh_13 = paramiko.SSHClient()
            self.ssh_13.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_13.connect('192.168.100.23', port=22, username=self.user_13, password=self.decrypted_ssh_13)
            self.stdin_13, self.stdout_13, self.stderr_13 = self.ssh_13.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_13 = self.stdout_13.read().decode()
            if self.output_13:
                self.date_13 = datetime.datetime.now()
                self.file_13 = open('log_status_ssh.txt', 'a')
                self.file_13.write(str(self.date_13) + " status: " + str(self.alive_13) + " Appliance: " + str(self.appliance_13) + ' SSH: ' + str(self.output_13))
                self.file_13.close()
                print("13")
                pass
            pass
        except:
            self.alive_13 = 'Down'
            self.date_13 = datetime.datetime.now()
            self.file_13 = open('log_status_ssh.txt', 'a')
            self.file_13.write(str(self.date_13) + " status: " + str(self.alive_13) + " Appliance: " + str(self.appliance_13) + "\n")
            self.file_13.close()
            self.sound = self.sound + 1
        self.Create_Json()

    def Commands_14(self):
        self.Encrypt_14()
        self.Decrypt_14()
        try:
            self.list_14 = []
            self.alive_14 = 'Up'
            self.ssh_14 = paramiko.SSHClient()
            self.ssh_14.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_14.connect('192.168.100.23', port=22, username=self.user_14, password=self.decrypted_ssh_14)
            self.stdin_14, self.stdout_14, self.stderr_14 = self.ssh_14.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_14 = self.stdout_14.read().decode()
            if self.output_14:
                self.date_14 = datetime.datetime.now()
                self.file_14 = open('log_status_ssh.txt', 'a')
                self.file_14.write(str(self.date_14) + " status: " + str(self.alive_14) + " Appliance: " + str(self.appliance_14) + ' SSH: ' + str(self.output_14))
                self.file_14.close()
                print("14")
                pass
            pass
        except:
            self.alive_14 = 'Down'
            self.date_14 = datetime.datetime.now()
            self.file_14 = open('log_status_ssh.txt', 'a')
            self.file_14.write(str(self.date_14) + " status: " + str(self.alive_14) + " Appliance: " + str(self.appliance_14) + "\n")
            self.file_14.close()
            self.sound = self.sound + 1
        self.Create_Json()

    def Commands_15(self):
        self.Encrypt_15()
        self.Decrypt_15()
        try:
            self.list_15 = []
            self.alive_15 = 'Up'
            self.ssh_15 = paramiko.SSHClient()
            self.ssh_15.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_15.connect('192.168.100.23', port=22, username=self.user_15, password=self.decrypted_ssh_15)
            self.stdin_15, self.stdout_15, self.stderr_15 = self.ssh_15.exec_command("uptime | awk '{print $1}' FS=',' | cut -c13-22")
            self.output_15 = self.stdout_15.read().decode()
            if self.output_15:
                self.date_15 = datetime.datetime.now()
                self.file_15 = open('log_status_ssh.txt', 'a')
                self.file_15.write(str(self.date_15) + " status: " + str(self.alive_15) + " Appliance: " + str(self.appliance_15) + ' SSH: ' + str(self.output_15))
                self.file_15.close()
                print("15")
                pass
            pass
        except:
            self.alive_15 = 'Down'
            self.date_15 = datetime.datetime.now()
            self.file_15 = open('log_status_ssh.txt', 'a')
            self.file_15.write(str(self.date_15) + " status: " + str(self.alive_15) + " Appliance: " + str(self.appliance_15) + "\n")
            self.file_15.close()
            self.sound = self.sound + 1
        self.Create_Json()

        time.sleep(10)

    def Create_Json(self):
        self.data = {
            'ADO1': self.alive_1,
            'Status_1': self.output_1,
            'ADO2': self.alive_2,
            'Status_2': self.output_2,
            'ADO3': self.alive_3,
            'Status_3': self.output_3,
            'ADO4': self.alive_4,
            'Status_4': self.output_4,
            'ADO5': self.alive_5,
            'Status_5': self.output_5,
            'ADO6': self.alive_6,
            'Status_6': self.output_6,
            'ADO7': self.alive_7,
            'Status_7': self.output_7,
            'ADO8': self.alive_8,
            'Status_8': self.output_8,
            'ADO9': self.alive_9,
            'Status_9': self.output_9,
            'ADO10': self.alive_10,
            'Status_10': self.output_10,
            'ADO11': self.alive_11,
            'Status_11': self.output_11,
            'ADO12': self.alive_12,
            'Status_12': self.output_12,
            'ADO13': self.alive_13,
            'Status_13': self.output_13,
            'ADO14': self.alive_14,
            'Status_14': self.output_14,
            'ADO15': self.alive_15,
            'Status_15': self.output_15
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
        self.sound = 0
        
if __name__ == '__main__':
    user_1 = input('AD01 >> ')
    password_1 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_2 = input('AD02 >> ')
    password_2 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_3 = input('AD03 >> ')
    password_3 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_4 = input('AD04 >> ')
    password_4 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_5 = input('AD05 >> ')
    password_5 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_6 = input('AD06 >> ')
    password_6 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_7 = input('AD07 >> ')
    password_7 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_8 = input('AD08 >> ')
    password_8 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_9 = input('AD09 >> ')
    password_9 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_10 = input('AD010 >> ')
    password_10 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_11 = input('AD011 >> ')
    password_11 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_12 = input('AD012 >> ')
    password_12 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_13 = input('AD013 >> ')
    password_13 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_14 = input('AD014 >> ')
    password_14 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    user_15 = input('AD015 >> ')
    password_15 = getpass.getpass('PASSWORD >> ').encode('utf-8')

    Submit = SSH(user_1= user_1, password_1 = password_1, user_2 = user_2, password_2 = password_2, user_3 = user_3, password_3 = password_3, user_4 = user_4, password_4 = password_4, user_5 = user_5, password_5 = password_5, user_6 = user_6, password_6 = password_6, user_7 = user_7, password_7 = password_7, user_8 = user_8, password_8 = password_8, user_9 = user_9, password_9 = password_9, user_10 = user_10, password_10 = password_10, user_11 = user_11, password_11 = password_11, user_12 = user_12, password_12 = password_12, user_13 = user_13, password_13 = password_13, user_14 = user_14, password_14 = password_14, user_15 = user_15, password_15 = password_15)