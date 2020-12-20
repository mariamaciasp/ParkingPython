# Importamos la libreria Pillow
from PIL import Image

# Importamos Pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrimos la imagen
im = Image.open("./Imagenes/img02.jpg")
# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con Pillow
texto = pytesseract.image_to_string(im, lang='eng', config="--psm 6")
#varnum= pytesseract.image_to_string(Image.open('./Imagenes/img03.jpg'),config='-psm 6')
#print(varnum)
# Mostramos el resultado
print(texto)
