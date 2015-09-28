#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random

class FaceGenetics(object):

    def __init__(self, chr1 = None, chr2 = None):
        if chr1 == None and chr2 == None:
        ##################################
            def chr_gene(times):
                test = ''
                for i in range(times):
                    test += str(random.randint(0, 1))
                return test
        ###################################
            self.chr1 = chr_gene(10000)
            self.chr2 = chr_gene(10000)
        else:
            self.chr1 = chr1
            self.chr2 = chr2

    def splitter(self, spl):
        self.chr1_spl = self.chr1.split(spl)
        self.chr2_spl = self.chr2.split(spl)

fg = FaceGenetics()
fg.splitter('101010')
print len(fg.chr1_spl)
print len(fg.chr2_spl)



