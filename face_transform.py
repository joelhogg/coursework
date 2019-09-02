import cv2
import os
import glob
import time

img_dir ="michelle_obama___Google_Search"
data_path = os.path.join(img_dir, "*g")
files = glob.glob(data_path)
data= []
faces_list = []

save = True #####modify here , True will save modified images

for f1 in files:
    img = cv2.imread(f1)
    data.append(img) #data is now a list of all images

for i in range(len(data)):
    img_1 = data[i]
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        #cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        img_temp_1 = (img_1[y:(y+h), x:(x+w)])
        img_temp_1 = cv2.resize(img_temp_1, (128,128))
        faces_list.append(img_temp_1)
        
    if save != True:
        for img_2 in faces_list:
            cv2.imshow("Extract",img_2)
            cv2.waitKey(0)
            
    elif save == True:
        n = 0
        checks = []
        for img_3 in faces_list:
            n += 1
            check_write = cv2.imwrite("face_mobama/img"+str(n)+".png",img_3)
            checks.append(check_write)

        if (False in checks) == False:
            print("all images stores sucsessfully")
        else:
            print("error storing an image")
    
    
    
    
