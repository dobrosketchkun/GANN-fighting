#-*-coding:utf8;-*-

from PIL import Image
from FaceImage import FaceImage

class Background(FaceImage):
    def __init__(self):
        #Размер бэкграунда взят с потолка, потом уточнить
        self.bc_w = 1500
        self.bc_h = 1500
        super(Background, self).__init__(self)
        self.image =  Image.new('RGBA', (self.bc_w, self.bc_h), (220, 220, 220, 255))
        self.prop()

    def paste(self, pasted, (x,y)):
        self.image.paste(pasted.image, (x,y), mask = pasted.image.split()[3])
        self.prop()