import cv2
import numpy as np
import os
import re
from PIL import Image
import pytesseract
#face_cascade = cv2.CascadeClassifier('cars.xml')
ncars = 0
cam = cv2.VideoCapture(0) 
try: 
    if not os.path.exists('data'): 
        os.makedirs('data') 
except OSError: 
    print ('Error: Creating directory of data') 
currentframe = 0
while(True):
    ret,frame = cam.read() 
    if ret:
            name="OUTPUT"+str(currentframe)+".jpg"
            print ('Creating...' + name)
            # writing the extracted images 
            cv2.imwrite(name, frame)
            cv2.imshow("window",frame)
            currentframe += 1
            cv2.waitKey(5)
            if currentframe==10:
                break
            #edge detection
            fileName = ['9','8','7','6','5','4','3','2','1','0']
            img = frame

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)

            kernel = np.ones((5,5),np.uint8)
            erosion = cv2.erode(gray,kernel,iterations = 2)
            kernel = np.ones((4,4),np.uint8)
            dilation = cv2.dilate(erosion,kernel,iterations = 2)

            edged = cv2.Canny(dilation, 30, 200)
            cv2.imshow('frame', edged)

            contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            rects = [cv2.boundingRect(cnt) for cnt in contours]
            rects = sorted(rects,key=lambda  x:x[1],reverse=True)

            i = -1
            j = 1
            y_old = 5000
            x_old = 5000
            print(rects)
            for rect in rects:
                x,y,w,h = rect
                area = w * h
                print(area)

                if area > 25000 and area < 100000:

                    if (y_old - y) > 200:
                        i += 1
                        y_old = y

                        if abs(x_old - x) > 300:
                            x_old = x
                            x,y,w,h = rect

                            out = img[y+10:y+h-10,x+10:x+w-10]
                            cv2.imwrite(fileName[i] + '_' + str(j) + '.jpeg', out)
            #cv2.imshow('frame', out)
                            j+=1

           #image to text conversion
            text = pytesseract.image_to_string(Image.open(name))
            print(text)
            test_string=text  
            print("The original string : " + test_string)   
            temp = re.findall(r'\d+', test_string) 
            #result = list(map(print,temp))
            print("the number extracted is:",temp)
            ini_string = text
            print ("initial string : ", ini_string) 
            res1 = " "  
            print ("first result: ", ini_string[0:2])       
    else: 
        break
  

cam.release() 
cv2.destroyAllWindows() 







































'''text = pytesseract.image_to_string(Image.open("8_6.jpeg"))
print(text

text = pytesseract.image_to_string(Image.open("9_2.jpeg"))
print(text)

      
text = pytesseract.image_to_string(Image.open("8_3.jpeg"))
print(text)

text = pytesseract.image_to_string(Image.open("8_4.jpeg"))
print(text)
text = pytesseract.image_to_string(Image.open("8_5.jpeg"))
print(text)
text = pytesseract.image_to_string(Image.open("9_1.jpeg"))
print(text)'''

