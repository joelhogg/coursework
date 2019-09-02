import cv2
import os
import glob

lname = "johnson"



img_dir = "face_"+lname
data_path = os.path.join(img_dir, "*g")
files = glob.glob(data_path)
data= []


for f1 in files:
    img = cv2.imread(f1)
    data.append(img)

n=0
for img_2 in data:
    n+=1
    cv2.imwrite("face_"+lname+"/img"+str(n)+".png",img_2)
