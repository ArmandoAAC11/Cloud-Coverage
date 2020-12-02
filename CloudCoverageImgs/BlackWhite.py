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
    im = Image.open(ruta)
    secuenciadepixeles=im.getdata()
    listadepixeles=list(secuenciadepixeles)
    print(listadepixeles)
#
def blanco_negro(imagen):
    ruta = ("./"+imagen)
    imagen = Image.open(ruta)
    # imagen.show()
    mascara = Image.new("L",(4368,2912),0)
    dibuja = ImageDraw.Draw(mascara)
    dibuja.ellipse((860,132,3508,2780), fill=255)
    imagen.putalpha(mascara)
    imagen2=imagen.crop((860,132,3508,2780))
    imagen2.show()
    i = 0
    while i < imagen2.size[0]:
        j = 0
        while j < imagen2.size[1]:
            r,g,b,a = imagen2.getpixel((i, j))
            try:
                proporcion = r/b
            except ZeroDivisionError:
                proporcion = 0
            if proporcion < 0.95:
                # pone el pixel el negro
                imagen2.putpixel((i,j),(0,0,0))
            else:
                #pone el pixel en blanco
                imagen2.putpixel((i,j),(255,255,255))
            j+= 1
        i+= 1
    imagen2.save("./kkkk.png")
    imagen2.show()


