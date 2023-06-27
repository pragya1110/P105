import os
import cv2

path="IMG"

img=[]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        file_name = path+'/'+file

        img.append(file_name)

#print(img)

count=len(img)
#print(count)

frame=cv2.imread(img[0])

h,w,c=frame.shape
size=(w,h)

#print(size)

out=cv2.VideoWriter("proj.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
     out.write(cv2.imread(img[i]))

out.release()
print("done")