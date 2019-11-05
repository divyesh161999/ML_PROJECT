# Importing all necessary libraries 
import cv2 
import os
import re
from PIL import Image
import pytesseract
import math

  
# Read the video from specified path 
cam = cv2.VideoCapture(0) 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret:
 
            #image = cv2.imread("image.jpg")


            text = pytesseract.image_to_string(Image.open("public.jpg"))
            print(text)

                    # Python3 code to demonstrate 
            # getting numbers from string  
            # using re.findall() 
            
              
            # initializing string  
            #test_string = "MH 13 RS 0027"
            test_string=text
              
            # printing original string  
            #print("The original string : " + test_string) 
              
            # using re.findall() 
            # getting numbers from string  
            #temp = re.findall(r'\d+', test_string) 
           # result = list(map(print,temp))
            #print("the number extracted is:",temp)
            # print result 
            #print("The numbers list is : " + str(res))
            ###############################################
            ###########################################
            # Python code to demonstrate 
            # to get characters in a string 
            # if present 
              
            # initialising string 
            ini_string = text
              
            # printing string and its length 
            print ("initial string : ", ini_string) 
              
            # code to find characters in string 
            res1 = " " 
            #for i in ini_string: 
                #if i.isalpha(): 
                    #res1 = "".join([res1, i]) 
              
              
            # printing resultant string
            
           # print ("first result: ", ini_string[0:2])
            #print ("first result: ", ini_string[11:15])
            extracted=ini_string[11:15]
            print(extracted.isnumeric())
            
            break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
