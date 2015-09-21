#-*-coding:utf8;-*-
#qpy:2
#qpy:console
import random
import os



big_sum = 0
big_times = 80
#print "This is console module"

##
##for item in [str(bin(i))[2:] for i in range(64)]:
##    for i in range(big_times):
##        gene = ""
##        times = 10000
##        for i in range(times):
##            gene += random.choice("01")
##        #print gene
##        t = gene.split(item)
##        #print t
##
##        sum = 0
##        for num in t:
##           sum += len(num)
##        sred = float(sum/len(t))
##        big_sum += sred
##
##    print item + ':', big_sum/big_times


##from PIL import Image
##from PIL import PSDraw
##
##im = Image.open("player.jpg")
##title = "Play"
##box = (1*72, 2*72, 7*72, 10*72) # in points
##
##ps = PSDraw.PSDraw() # default is sys.stdout
##ps.begin_document(title)
##
### draw the image (75 dpi)
##ps.image(box, im, 75)
##ps.rectangle(box)
##
### draw title
##ps.setfont("HelveticaNarrow-Bold", 36)
##ps.text((3*72, 4*72), title)
##ps.end_document()

path = os.path.dirname(__file__)
path_pix = path + '/test/deface_layers/pixel/'

from PIL import Image

##img1 = Image.open(path + '/test/1.png')
##img2 = Image.open(path + '/test/2.png')
##img2.load()
##img1.paste(img2, (300,220), mask = img2.split()[3])
##img1.save(path + '/test/out.png')
img = Image.open(path_pix + 'all.png')
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
    p = Image.open(path_pix + part + '.png')
    p.load()
    img.paste(p, (0,0),mask = p.split()[3])


##ch_w, ch_h = chin.size
##new_ch_w = img_w - ch_w
##new_ch_h = img_h - ch_h
##
##print new_ch_w,new_ch_h
##img.paste(chin, (new_ch_w,new_ch_h))


#background = Image.new('RGBA', (950, 1100), (255, 255, 255, 255))
##
##bg_w, bg_h = background.size
##offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
##background.paste(img, offset)
img.save(path + '/test/out.png')