import cv2 
import os
import re
import csv
from PIL import Image
import pytesseract
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
             #code to save images 
            # if video is still left continue creating images 
            #name = './data/frame' + str(currentframe) + '.jpg'
            name="OUTPUT"+str(currentframe)+".jpg"
            print ('Creating...' + name) 
  
            # writing the extracted images 
            cv2.imwrite(name, frame)
            cv2.imshow("window",frame)
  
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
            cv2.waitKey(5)
            if currentframe==5:
                break
            text = pytesseract.image_to_string(Image.open(name))
            #print(text)
            test_string=text  
            print("The original string : " + test_string)   
            temp = re.findall(r'\d+', test_string) 
            #result = list(map(print,temp))
            print("the number extracted is:",temp)
            ini_string = text
            #print ("initial string : ", ini_string) 
            res1 = " "  
            print ("first result: ", ini_string[0:2])
            print ("last four numbers: ", ini_string[9:13])
            #extracted=ini_string[12:16]
            #print(extracted.isnumeric())
            with open('database.csv', 'rt') as f:
              file = csv.reader(f)
              for row in file:
                if (ini_string[9:13]==row[1]):
                  print(row)

           
        
    else: 
        break
  

cam.release() 
cv2.destroyAllWindows() 
