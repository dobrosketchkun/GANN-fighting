#-*-coding:utf8;-*-

import random
import os
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


face_dict = parts_preload()


face_w = max(face_dict['chin'].size[0], face_dict['front'].size[0], face_dict['forehead'].size[0])
face_h = face_dict['chin'].size[1] + face_dict['front'].size[1] + face_dict['forehead'].size[1]

print face_h, face_w



for key in face_dict:
    face_dict[key].load

background = Image.new('RGBA', (face_w, face_h), (220, 220, 220, 255))

background.paste(face_dict['forehead'], (0,0), mask = face_dict['forehead'].split()[3])


background.paste(face_dict['front'], ((face_w - face_dict['front'].size[0])/2, face_dict['forehead'].size[1]-20), mask = face_dict['front'].split()[3])

background.paste(face_dict['chin'], ((face_w - face_dict['chin'].size[0])/2, face_dict['front'].size[1] + face_dict['forehead'].size[1]-50), mask = face_dict['chin'].split()[3])

background.show()