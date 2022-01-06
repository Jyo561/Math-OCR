import cv2 as cv
import pytesseract 

pytesseract.pytesseract.tesseract_cmd=r'/usr/bin/tesseract'
cong = r'--oem 3 --psm 6 outputbase digits'
img = cv.imread('./IMG_20211223_193631.jpg')
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgt=cv.blur(img,(4,1),8)
config='-l eng + equ'
custom_config = r'--oem 3 --psm 6'

canny=cv.Canny(imgt,125,175)
print(pytesseract.image_to_string(canny,config=custom_config))
print(pytesseract.image_to_string(canny,config=cong))
cv.imshow('Canny',canny)

cv.waitKey(0)
