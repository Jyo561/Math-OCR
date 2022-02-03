import cv2 as cv
import numpy as np
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd=r'/usr/bin/tesseract'
os.environ['TESSDATA_PREFIX']='/usr/share/tessdata/'
imgpath="./"+"anh6.png"
tub_kernel=(2,3)
img=cv.imread(imgpath)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
kernel=np.ones(tub_kernel,np.uint8)
gray=cv.dilate(gray,kernel,iterations=1)
gray=cv.erode(gray,kernel,iterations=2)
_,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
#cv.imwrite("./"+"thres.jpg",gray)

result=pytesseract.image_to_string(gray).strip()

if not result or len(result.split(" ")) < 5:
    tub_kernel=(1,3)
    img=cv.imread(imgpath)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel=np.ones(tub_kernel,np.uint8)
    gray=cv.dilate(gray,kernel,iterations=1)
    gray=cv.erode(gray,kernel,iterations=2)
    _,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #cv.imwrite("./"+"thres.jpg",gray)
    result=pytesseract.image_to_string(gray).strip()
# Try one more
if not result or len(result.split(" ")) < 5:
    tub_kernel=(4,3)
    img=cv.imread(imgpath)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel=np.ones(tub_kernel,np.uint8)
    gray=cv.dilate(gray,kernel,iterations=1)
    gray=cv.erode(gray,kernel,iterations=2)
    _,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #cv.imwrite("./"+"thres.jpg",gray)
    result=pytesseract.image_to_string(gray).strip()
#print(eval(result))
if not result or len(result.split(" ")) < 5:
    tub_kernel=(2,3)
    img=cv.imread(imgpath)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel=np.ones(tub_kernel,np.uint8)
    gray=cv.dilate(gray,kernel,iterations=5)
    gray=cv.erode(gray,kernel,iterations=1)
    _,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #cv.imwrite("./"+"thres.jpg",gray)
    result=pytesseract.image_to_string(gray).strip()
if not result or len(result.split(" ")) < 5:
    tub_kernel=(1,3)
    img=cv.imread(imgpath)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel=np.ones(tub_kernel,np.uint8)
    gray=cv.dilate(gray,kernel,iterations=4)
    gray=cv.erode(gray,kernel,iterations=0)
    _,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #cv.imwrite("./"+"thres.jpg",gray)
    result=pytesseract.image_to_string(gray).strip()
if not result or len(result.split(" ")) < 5:
    tub_kernel=(1,3)
    img=cv.imread(imgpath)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #gray=cv.Canny(gray,125,205)
    kernel=np.ones(tub_kernel,np.uint8)
    gray=cv.dilate(gray,kernel,iterations=2)
    gray=cv.erode(gray,kernel,iterations=3)
    _,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #cv.imwrite("./"+"thres.jpg",gray)
    result=pytesseract.image_to_string(gray).strip()
if not result or len(result.split(" ")) < 5:
    tub_kernel=(2,3)
    img=cv.imread(imgpath)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #gray=cv.Canny(gray,125,205)
    kernel=np.ones(tub_kernel,np.uint8)
    gray=cv.dilate(gray,kernel,iterations=5)
    gray=cv.erode(gray,kernel,iterations=1)
    _,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #cv.imwrite("./"+"thres.jpg",gray)
    result=pytesseract.image_to_string(gray).strip()
if not result or len(result.split(" ")) < 5:
    tub_kernel=(1,3)
    img=cv.imread(imgpath)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #gray=cv.Canny(gray,125,205)
    kernel=np.ones(tub_kernel,np.uint8)
    gray=cv.dilate(gray,kernel,iterations=4)
    gray=cv.erode(gray,kernel,iterations=3)
    _,gray=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #cv.imwrite("./"+"thres.jpg",gray)
    result=pytesseract.image_to_string(gray).strip()
cv.imshow('Gray',gray)
if "=" in result:
    erm=result.find("=")
    result=result[0:erm]
if "x" in result:
    erm=result.find("x")
    result=result[0:erm]+"*"+result[erm+1:]
print(eval(result))
#print(result)
cv.waitKey(0)