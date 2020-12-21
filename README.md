# ParkingPython
El proyecto consiste en realizar una aplicación para gestionar un parking

El parking cuenta con dos zonas:


1- Zona cliente: Aquí podremos insertar y retirar vehículos de clientes abonados y normales.

2- Zona administrador: Podremos realizar las consultas relacionadas con el parking, entre ellas podemos encontrar consultar estado del parking, facturación del mismo, consulta abonos anuales, gestionar los diferentes abonos (alta, baja y modificar (abono o datos abonados), consultar caducidad de abonos tanto mensual como en los próximos 10 días). Por último, he agregado una opción de consulta de imágenes, en ella se leerás las imagenes tomadas de los tres últimos vehículos ingresados en el parking (estas imagenes están ya introducidas en el directorio "Imagenes")

##ANOTACIONES IMPORTANTES:

Si no se tiene instalado en el equipo las librerías necesarias para la lectura de imágenes, este fallará, se debe tener instalado previamente "pytesseract" y "opencv" con las versiones correspondientes (en el caso de cv no tiene por qué ser la última versión!!!). ¡¡El programa compila correctamente!!

En cuanto a esto también puede dar fallo la línea 9 de Repository/imagen_repository que es la siguiente: "pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'", comentar y en el caso de querer ejecutar la opción asegurarse de que la ruta donde esté tesseract.exe en el ordenador sea la correcta.


Si esto da demasiados problemas puede obviar la opción 6 del menu administrador, pero el código funcionará correctamente si el entorno está preparado.

###Acceso zona administrador:
El programa cuenta con dos usuarios administradores:

Usuario: admin, password: 1234
Usuario: maria1, password: 1234

Por último, si necesita hacer alguna comprobación respecto al abonado que ya está introducido en el sistema, necesitará conocer el PIN, para ello lo más sencillo es descomentar la línea 115 del main, así podremos ver todos los abonados dados de alta





