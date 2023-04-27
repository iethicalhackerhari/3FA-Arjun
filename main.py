import face_recognition_code
import otp
import pandas as pd
import os 
from cipher import encryption, decryption
def createDatabase(names = ['SREEHARI'], usernames = ['sree'], passwords = ['sree']):
    new_db = pd.DataFrame()
    new_db['name'] = names
    new_db['username'] = usernames
    new_db['password'] = passwords
    
    new_db.to_csv('new_database.csv')

def getFirstVerificationInputs():
    username = input("Enter your username: ").lower()
    password = input("Enter the password: ")
    
    return username, password

def checkCorrect(database_name , name, username, password):
    data = pd.read_csv(database_name)

    usernameList = data['username'].tolist()
    passwordList = data['password'].tolist()
    # check if username in new_database.csv
    flag_pass = 0
    flag_username = 0
    if username in usernameList:
        flag_username = 1
        ListIndex = usernameList.index(username)
        correct_pass = passwordList[ListIndex]

        if correct_pass == password:
            flag_pass = 1
    
    if flag_username == 0:
        print("Username not found...")
        print("Enter registered username...")
        print()
        firstFactor()

    elif flag_pass == 1:
        print("Password Correct...")
        print("Level1 verified...")
        print()
        # go to next level
        # secondVerification()

    else:
        print("Password incorrect try again...")
        print()
        # try again - 1st level
        firstFactor()
        # done

def firstFactor(name):

    username, password = getFirstVerificationInputs()
    correct_flag = checkCorrect('new_database.csv', name, username, password)

def secondFactor(receiverMail):

    # OTP PHASE
    otp_object = otp.OTP(receiver_mail = receiverMail)
    otp_object.sendOTP()
    otp_object.verifyOTP()
    
def showPasswords(name):
    decryption('arjun',f'D:/python/arjun/3FA/secretVault/{name}.txt')
    osCommandString = f"notepad.exe D:/python/arjun/3FA/secretVault/{name}.txt"
    os.system(osCommandString)
    encryption('arjun',f'D:/python/arjun/3FA/secretVault/{name}.txt')
    

def main():
    createDatabase()
    
    # 1st factor
    print("---------------------- 1st Factor ----------------------")
    name = str(input("Enter your name: "))
    firstFactor(name)

    # 2nd factor
    print("---------------------- 2nd Factor ----------------------")
    receiverMail = str(input("Enter your MAIL ID for verification: "))
    secondFactor(receiverMail)
    print()
    # 3rd factor
    print("---------------------- 3rd Factor ----------------------")
    model = face_recognition_code.FaceRecognition()
    nameFromModel = model.recognize_face()

    print("Model name: ",nameFromModel)
    print("Input name: ", name)
    
    if name.lower() == nameFromModel.lower():
        print("Face recognized...")
        print("Verified...")
        print("Welcome ",name, " !!!")
        showPasswords(name.lower())


if __name__ == '__main__':
    main()