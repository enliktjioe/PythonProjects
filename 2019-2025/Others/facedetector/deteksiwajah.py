import numpy as np
import cv2 as cv
 
wajah=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv.imread('gambar/Heavenly-Forest.jpg')
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 
deteksi_wajah=wajah.detectMultiScale(img_gray,1.1,5)
font=cv.FONT_HERSHEY_SIMPLEX
jumlah=0
 
for(x,y,w,h) in deteksi_wajah:
    jumlah=jumlah+1
    cv.putText(img,"Wajah",(x,y-10),font,0.75,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=img_gray[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
 
cv.putText(img,"Jumlah wajah ada : "+str(jumlah)+ " buah",(10,40),font,1,(255,255,50),2,cv.LINE_AA)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()