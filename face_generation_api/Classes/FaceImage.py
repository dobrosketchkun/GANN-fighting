#-*-coding:utf8;-*-
from PIL import Image


class FaceImage(object):
    def prop(self):
        self.size = self.image.size
        self.w, self.h = self.size
        self.center = (self.image.size[0]/2, self.image.size[1]/2)
        self.top_center = (self.image.size[0]/2, 0)
        self.bottom_center = (self.image.size[0]/2, self.image.size[1])
        self.left_center = (0, self.image.size[1]/2)
        self.right_center = (self.image.size[0], self.image.size[1]/2)
        self.image.load()
    def __init__(self, image):
        try:
            self.image = Image.open(image)
        except:
            print "No image in FaceImage.class"
    def show(self):
        self.image.show()
        self.prop()
    def save(self, path):
        self.image.save(path)