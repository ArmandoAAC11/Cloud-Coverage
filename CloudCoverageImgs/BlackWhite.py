import time
from PIL import Image, ImageDraw
import os

def mascara(im):
    ruta = ("./"+im)
    print(os.getcwd())
    imagen = Image.open(ruta)

    mascara = Image.new("L",(4368,2912),0)
    dibuja = ImageDraw.Draw(mascara)
    dibuja.ellipse((860,132,3508,2780), fill=255)
    imagen.putalpha(mascara)
    imagen=imagen.crop((860,132,3508,2780))
    imagen.save("./S-crop.png")
    imagen.show()

def abrir_imagen(imagen):
    ruta = ("./"+imagen)
    imagen = Image.open(ruta)
    imagen.show()

def blanco_negro(im):
    ruta = ("./"+im)
    imagen = Image.open(ruta)
    imagen.show()
    imagen2 = imagen
    i = 0
    while i < imagen2.size[0]:
        j = 0
        while j < imagen2.size[1]:
            r,g,b,a = imagen2.getpixel((i, j))
            proporcion = r/b
            if proporcion < 0.95:
                imagen2.putpixel((i,j),(0,0,0))
            else:
                imagen2.putpixel((i,j),(255,255,255))
            j+= 1
        i+= 1
    imagen2.show()