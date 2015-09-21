#-*-coding:utf8;-*-

import random
import os
from PIL import Image

path = os.path.dirname(__file__)
path_trim = path + '/test/trim/'
#path_pix = path + '/test/deface_layers/pixel/'



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


def test_no_trim():
    """
    Функция собирает из частей лицо. Для теста изображений без трима
    """
    img = Image.open(path + '/test/deface_layers/pixel/' + 'all.png')
    img_w, img_h = img.size
    #chin = Image.open(path_pix + "chin.png")
    face_list = ['chin',
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


    for part in face_list:
        p = Image.open(path + '/test/deface_layers/pixel/' + part + '.png')
        p.load()
        img.paste(p, (0,0),mask = p.split()[3])
        img.save(path + '/test/out.png')


def parts_preload():
    """
    Презагружает все составные части и возвращает словарь
    формата {'part': экземпляр класса изображения}
    """
    return {item: Image.open(path_trim + item + '.png') for item in FACE_LIST}


##face_dict = parts_preload()
##
####face_origin = ['chin', 'front', 'forehead']
##
##face_h = face_dict['chin'].size[0] + face_dict['front'].size[0] + face_dict['forehead'].size[0]
##face_w = face_dict['chin'].size[1] + face_dict['front'].size[1] + face_dict['forehead'].size[1]
##
##
##
####for item in face_origin:
####
####    part = face_dict[item]
####    part_w, part_h = part.size
####    face_h += part_h
####    face_w += part_w
####
####    print 'Parts: ',  part_w, part_h
##
##print face_h, face_w



import matfunc as mt
import numpy as np

def perspective_coefficients(oldplane, newplane):
    """
    Calculates and returns the transform coefficients needed for a perspective
    transform, ie tilting an image in 3D.
    Note: it is not very obvious how to set the oldplane and newplane arguments
    in order to tilt an image the way one wants. Need to make the arguments more
    user-friendly and handle the oldplane/newplane behind the scenes.
    Some hints on how to do that at http://www.cs.utexas.edu/~fussell/courses/cs384g/lectures/lecture20-Z_buffer_pipeline.pdf

    | **option** | **description**
    | --- | ---
    | oldplane | a list of four old xy coordinate pairs
    | newplane | four points in the new plane corresponding to the old points

    """
    # first find the transform coefficients, thanks to http://stackoverflow.com/questions/14177744/how-does-perspective-transformation-work-in-pil
    pb,pa = oldplane,newplane
    grid = []
    for p1,p2 in zip(pa, pb):
        grid.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        grid.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    # then do some matrix magic
    A = mt.Matrix(grid)
    B = mt.Vec([xory for xy in pb for xory in xy])
    AT = A.tr()
    ATA = AT.mmul(A)
    gridinv = ATA.inverse()
    invAT = gridinv.mmul(AT)
    res = invAT.mmul(B)
    a,b,c,d,e,f,g,h = res.flatten()

    # finito
    return a,b,c,d,e,f,g,h


x11 = 0; x12 = 0.5
y11 = 0; y12 = 0
x21 = 1; x22 = 1
y21 = 1; y22 = 1
x31 = 0; x32 = 0.5
y31 = 1; y32 = 1
x41 = 1; x42 = 1
y41 = 0; y42 = 0

per_coef = perspective_coefficients([(x11,y11),(x21,y21),(x31,y31),(x41,y41)],
                                    [(x12,y12),(x22,y22),(x32,y32),(x42,y42)])


img = Image.open(path_trim + 'chin.png')

width, height = img.size
m = -0.5
xshift = abs(m) * width
new_width = width + int(round(xshift))
img = img.transform((800, 800), Image.PERSPECTIVE,
    per_coef, Image.BICUBIC)
 #       (1, m, -xshift if m > 0 else 0, 0, 1, 1), Image.BICUBIC)


#ВАЖНАЯ ЧАСТЬ, ДЕЛАЕТ ЧАСТЬ ТЕЛА НЕПРОЗРАЧНОЙ ПОСЛЕ ИСКАЖЕНИЯ
transimage = img
transparency = 255
size = img.size
I = np.asarray(transimage)  # (y, x, band)
maskmat = (I[:,:,0] | I[:,:,1] | I[:,:,2] == 0)
mask = np.ones(size, int).transpose() * transparency
mask[maskmat] = 0
mask = Image.fromarray(np.uint8(mask))
transimage.putalpha(mask)

#img.show()
img.save(path + '/test/out.png')
