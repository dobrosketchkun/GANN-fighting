#-*-coding:utf8;-*-

import random
import os
import copy
from PIL import Image

path = os.path.dirname(__file__)
path_trim = path + '/test/trim/'

FACE_LIST = ['chin',
            'chin_wrinkle',
            'front',
            'neck',
            'forehead',
            'left_eye',
            'left_eyebow',
            'left_eyelip',
            'right_eye',
            'right_eyebow',
            'right_eyelip',
            'up_lip',
            'down_lip',
            'nose',
            'left_ear',
            'right_ear']

def parts_preload():
    """
    Презагружает все составные части и возвращает словарь
    формата {'part': экземпляр класса изображения}
    """
    return {item: Image.open(path_trim + item + '.png') for item in FACE_LIST}


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




class FacePart(FaceImage):
    def __init__(self, image, name):
        super(FacePart, self).__init__(image)
        ##self.image = Image.open(image)
        self.name = name
        self.image.load()
        self.prop()

    def resize(self,w,h):
        self.image = self.image.resize((w,h), Image.BICUBIC)
        self.prop()
        #self.size = self.image.size



class Background(FaceImage):
    def __init__(self):
        self.bc_w = 1000
        self.bc_h = 1000
        super(Background, self).__init__(self)
        self.image =  Image.new('RGBA', (self.bc_w, self.bc_h), (220, 220, 220, 255))

        self.prop()

    def paste(self, pasted, (x,y)):
##        try:
##            if pasted.name == 'chin':
##                (x, y) = (self.center[0] - pasted.center[0], self.bc_h/2 - pasted.h)
##            else:
##                print 'Not chin'

        self.image.paste(pasted.image, (x,y), mask = pasted.image.split()[3])
##        except:
##            print 'Image should be .load() first'
        self.prop()


def Face_Parts_preload():
    """
    Презагружает все составные части и возвращает словарь
    формата {'part': экземпляр класса изображения}
    """
    return {item: FacePart(path_trim + item + '.png', item) for item in FACE_LIST}

face_dict = Face_Parts_preload()

#CHIN_X = 'chin_x = self.center[0] - pasted.center[0]'

background = Background()
#chin = face_dict['chin']

#background.paste(chin)

face_w_c = 1
forehead_h_c = 1
front_h_c = 1
chin_h_c = 1


def pasting(background, list_of_pasted):
    gap = 50
    for part in list_of_pasted:
        if part.name == 'forehead':
            part.resize(int(part.w * face_w_c), int(part.h * forehead_h_c))
            (x, y) = (background.center[0] - part.center[0], gap)

            background.paste(part, (x, y))

        if part.name == 'front':
            part.resize(int(part.w * face_w_c), int(part.h * front_h_c))
            (x, y) = (background.center[0] - part.center[0], face_dict['forehead'].h + gap)

            background.paste(part, (x, y))

        if part.name == 'chin':
            part.resize(int(part.w * face_w_c), int(part.h * chin_h_c))
            (x, y) = (background.center[0] - part.center[0],
            face_dict['forehead'].h + face_dict['front'].h + gap)

            background.paste(part, (x, y))



pasting(background, [face_dict['forehead'], face_dict['front'],face_dict['chin']])
background.show()



##        try:
##        if pasted.name == 'chin':
##            (x, y) = (self.center[0] - pasted.center[0], self.bc_h/2 - pasted.h)
##        else:
##            print 'Not chin'

##        self.image.paste(pasted.image, (x,y), mask = pasted.image.split()[3])

