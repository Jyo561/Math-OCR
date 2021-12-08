OCR has applications in a broad range of industries and functions. 
So, everything from scanning documents – bank statements, receipts,
handwritten documents, coupons, etc.,  to reading street signs in autonomous vehicles
– this all falls under the OCR umbrella.

OCR has two parts to it. 
The first part is text detection where the textual part within the image is determined. 
This localization of text within the image is important for the second part of OCR, 
text recognition, where the text is extracted from the image. 
Using these techniques together is how you can extract text from any image.
OCR has two parts to it.
The first part is text detection where the textual part within the image is determined.
This localization of text within the image is important for the second part of OCR, 
text recognition, where the text is extracted from the image. 
Using these techniques together is how you can extract text from any image.

Tesseract is an open-source OCR engine originally
developed as proprietary software by HP (Hewlett-Packard) but was later made open source in 2005. 
Google has since then adopted the project and sponsored its development.

As of today, Tesseract can detect over 100 languages and can process 
even right-to-left text such as Arabic or Hebrew! 
No wonder it is used by Google for text detection on mobile devices, 
in videos, and in Gmail’s image spam detection algorithm.

Once you have downloaded Tesseract onto your system, you easily run it from the command line using the following command:
tesseract <test_image> <output_file_name> -l <language(s)> --oem <mode> --psm <mode>

1.Langue (-l) – You can detect a single language or multiple languages with Tesseract
2.OCR engine mode (–oem) – As you already know, Tesseract 4 has both LSTM and Legacy OCR engines. 
However, there are 4 modes of valid operation modes based on their combination
3.Page Segmentation (–psm) – Can be adjusted according to the text in the image for better results

Pyteseract
However, instead of the command-line method, you could also use Pytesseract – a Python wrapper for Tesseract. 
Using this you can easily implement your own text recognizer using Tesseract OCR by writing a simple Python script.

You can download Pytesseract using the pip install pytesseract command.

The main function in Pytesseract is image_to_text() which takes the image 
and the command line options as its arguments:

# text recognition
import cv2
import pytesseract
# read image
im = cv2.imread('./test3.jpg')
# configurations
config = ('-l eng --oem 1 --psm 3')
# pytessercat
text = pytesseract.image_to_string(im, config=config)
# print text
text = text.split('\n')
print(text)



What are the Challenges with Tesseract?
It’s no secret that Tesseract is not perfect. 
It performs poorly when the image has a lot of noise or when the font of the 
language is one on which Tesseract OCR is not trained. 
Other conditions like brightness or skewness of text will also affect the performance of Tesseract. 
Nevertheless, it is a good starting point for text recognition with low efforts and high outputs.

Text Detection using OpenCV:
# preprocessing
# gray scale
def gray(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"./preprocess/img_gray.png",img)
    return img

# blur
def blur(img) :
    img_blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imwrite(r"./preprocess/img_blur.png",img)    
    return img_blur

# threshold
def threshold(img):
    #pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)[1]    
    cv2.imwrite(r"./preprocess/img_threshold.png",img)
    return img

Once you have done that, you can use OpenCV contours detection to detect contours
to extract chunks of data:
# Finding contours 
im_gray = gray(im)
im_blur = blur(im_gray)
im_thresh = threshold(im_blur)

contours, _ = cv2.findContours(im_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

Finally, you can apply text recognition on the contours that you got to predict the text:
# text detection
def contours_text(orig, img, contours):
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 

        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 255), 2) 
        
        cv2.imshow('cnt',rect)
        cv2.waitKey()

        # Cropping the text block for giving input to OCR 
        cropped = orig[y:y + h, x:x + w] 

        # Apply OCR on the cropped image 
        config = ('-l eng --oem 1 --psm 3')
        text = pytesseract.image_to_string(cropped, config=config) 

        print(text)