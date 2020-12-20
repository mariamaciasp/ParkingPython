from PIL import Image
import pytesseract
import re

class imagen_repository():


    def leer_imagen(self):

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img1 = Image.open("./Imagenes/img01.jpg")
        img2 = Image.open("./Imagenes/img02.jpg")
        img3 = Image.open("./Imagenes/img03.jpg")
        imagenes = [img1, img2, img3]
        matriculas = []
        for i in imagenes:
            texto = pytesseract.image_to_string(i, lang='eng', config="--psm 6")
            palabra = ""

            for j in texto:
                if(j.isdigit()):
                    palabra += j
                if(j.isalpha()):
                    palabra += j
            matriculas.append(palabra)

        for i in matriculas:
            print(i)
