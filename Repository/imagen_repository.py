from PIL import Image
import pytesseract
import cv2

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


    # mi no entender
    def leer_imagen2(self):

        image = cv2.imread('./Imagenes/imagen5.jpg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.blur(gray,(3,3))
        canny = cv2.Canny(gray,150,200)
        canny = cv2.dilate(canny,None,iterations=1)

        cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
          area = cv2.contourArea(c)

          x,y,w,h = cv2.boundingRect(c)
          epsilon = 0.09*cv2.arcLength(c,True)
          approx = cv2.approxPolyDP(c,epsilon,True)

          if len(approx)==4 and area>9000:
            #print('area=',area)
            #cv2.drawContours(image,[approx],0,(0,255,0),3)

            aspect_ratio = float(w)/h
            if aspect_ratio>2.4:
              matricula = gray[y:y + h, x:x + w]
              text = pytesseract.image_to_string(matricula, config='--psm 6')
              print('Matrícula: ',text)

