#-*-coding:utf8;-*-
#qpy:2
#qpy:console
import random
big_sum = 0
big_times = 80
#print "This is console module"
for i in range(big_times):
    gene = ""
    times = 10000
    for i in range(times):
        gene += random.choice("01")
    #print gene
    t = gene.split("1010")
    #print t

    sum = 0
    for num in t:
       sum += len(num)
    sred = float(sum/len(t))
    big_sum += sred

print big_sum/big_times