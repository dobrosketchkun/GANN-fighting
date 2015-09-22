#-*-coding:utf8;-*-

from PIL import Image
from FaceImage import FaceImage

class FacePart(FaceImage):
    def __init__(self, image, name):
        super(FacePart, self).__init__(image)
        self.image = Image.open(image)
        self.name = name
        self.image.load()
        self.prop()

    def resize(self,w,h):
        self.image = self.image.resize((w,h), Image.BICUBIC)
        self.prop()

    def rotate(self, angle):
        self.image = self.image.rotate(angle, expand=True)
        self.prop()