import cv2
from pytesseract import pytesseract

class OCR_Video():

    def __init__(self):
        pass

    def Video_OCR(self,Video_Path,Video_Name='Video'):
        Total=[]
        Cap = cv2.VideoCapture(Video_Path)
        while True:
            ret , frame = Cap.read()
            if ret == True :
                cv2.imshow(Video_Name,frame)
                Text=pytesseract.image_to_string(frame)
                print(Text)
                Total.append(Text)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                Cap.release()
                cv2.destroyAllWindows()