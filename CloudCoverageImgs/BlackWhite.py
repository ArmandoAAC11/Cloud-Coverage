from PIL import Image
import time
def abrir_imagen(imagen):
    tiempoInicial = time.time()
    ruta = ("/home/armandoaac/Descargas/CloudCoverageImgs/"+imagen)
    imagen = Image.open(ruta)
    imagen.show()
    tiempofin = time.time()
    print("Se tardo ", tiempofin - tiempoInicial, " segundos")
    print("jala chido")
def blanco_negro(imagen):
    ruta = ("/home/armandoaac/Descargas/CloudCoverageImgs/"+imagen)
    imagen = Image.open(ruta)
    imagen.show()
    imagen2 = imagen
    i = 0
    while i < imagen2.size[0]:
        j = 0
        while j < imagen2.size[1]:
            r,g, b = imagen2.getpixel((i, j))
            proporcion = (r+g+b)/3
            if proporcion < 242:
                imagen2.putpixel((i,j),(0,0,0))
            else:
                imagen2.putpixel((i,j),(255,255,255))
            j+= 1
        i+= 1
    imagen2.show()