#-*-coding:utf8;-*-
#qpy:2
#qpy:console
import random
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


from PIL import Image
from PIL import PSDraw

im = Image.open("player.jpg")
title = "Play"
box = (1*72, 2*72, 7*72, 10*72) # in points

ps = PSDraw.PSDraw() # default is sys.stdout
ps.begin_document(title)

# draw the image (75 dpi)
ps.image(box, im, 75)
ps.rectangle(box)

# draw title
ps.setfont("HelveticaNarrow-Bold", 36)
ps.text((3*72, 4*72), title)

ps.end_document()