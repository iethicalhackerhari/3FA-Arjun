import os
import math
import random
import smtplib


class OTP():

    def __init__(self, receiver_mail):
        self.msg = ""
        self.otp_code = 0
        self.senderMailID = "ismprojectdemo@gmail.com"
        self.sendPassword = 'gaef gnbs pqqa tjvg'
        self.recieverMailID = receiver_mail

    def sendOTP(self):
        digits = "0123456789"
        OTP = ""
        for i in range(6):
            OTP += digits[math.floor(random.random()*10)]
        emailmsg = OTP + " is your OTP"
        
        self.otp_code = int(OTP)
        self.msg = str(emailmsg)

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.senderMailID, self.sendPassword)
        server.sendmail(self.senderMailID, self.recieverMailID, self.msg)
        server.quit()

    def verifyOTP(self):
        a = int(input("Enter Your OTP >>: "))
        if a == self.otp_code:
            print("Verified")
        else:
            print("Please Check your OTP again")