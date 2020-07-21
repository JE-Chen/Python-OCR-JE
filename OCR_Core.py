from OCR import OCR
from OCR_Video import OCR_Video

class OCR_Core():

    def __init__(self):
        try:
            self.OCR=OCR()
        except Exception as Errr:
            print(Errr)