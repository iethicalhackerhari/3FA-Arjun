import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime

class FaceRecognition():
    def __init__(self, path = r'D:\python\arjun\3FA\data'):
        self.special_name = ''
        self.path = path
        self.images = []
        self.classNames = []
        self.count = 0
        
        print("Encoding in progress...")
        myList = os.listdir(self.path)
        for cls in myList:
            curImg = cv2.imread(f'{self.path}/{cls}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cls)[0])
        
        self.encodeListKnown = self.findEncodings()
        print('Encoding complete...')


    def findEncodings(self):
        encodeList = []
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def accessGranted(self, name):
        # with open(r'D:\python\arjun\3FA\attendance.csv','r+') as f:
        #     myDataList = f.readlines()
        #     nameList = []
        #     for line in myDataList:
        #         entry = line.split(',')
        #         nameList.append(entry[0])
        #     if name not in nameList:
        #         now = datetime.now()
        #         dtString = now.strftime('%H:%M:%S')
        #         f.writelines(f'\n{name},{dtString}')
        print("Welcome " + name )

    def recognize_face(self):
        
        hashTable = {}
        good_name = ""
        cap = cv2.VideoCapture(0)
        break_flag = False
        while True:
            if break_flag:
                break
            success, img = cap.read()
            imgSmall = cv2.resize(img, (0,0), None, 0.25,0.25)
            imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

            faceCurFrame = face_recognition.face_locations(imgSmall)
            encodesCurFrame = face_recognition.face_encodings(imgSmall, faceCurFrame)
            # print(len(faceCurFrame),len(encodesCurFrame))
            for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)
                # print(matches[matchIndex])
                if matches[matchIndex]:
                    name = self.classNames[matchIndex].upper()
                    # print(name)
                    if name not in hashTable.keys():
                        hashTable[name] = 0
                    else:
                        hashTable[name] += 1

                    if hashTable[name] > 10:
                        break_flag = True
                        good_name = name
                        break

                    y1,x2,y2,x1 = faceLoc
                    y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img, (x1,y1),(x2,y2), (0,255,0),2)
                    cv2.rectangle(img, (x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
                    self.accessGranted(name)
                    
            cv2.imshow("Webcam", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()    
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return good_name