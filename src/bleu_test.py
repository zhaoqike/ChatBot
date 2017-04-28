# -*- coding: utf8 -*-

import time
import nltk


path = "/home/zhaoqike/Documents/100_selected_result_zhaoqike.txt"

f = open(path,"r")
lines = f.readlines()
for line in lines:
    # print line
    parts = line.split('|')
    for p in parts:
        p = p.strip()
    # print parts
    print parts[2], parts[3]
    hyp = parts[2].split(' ')
    ref = parts[3].split(' ')
    hyp = filter(lambda x: x != '' and x != '…' and x != '！' and x != '？' and x != '，' and x != '。' and x != '、', hyp)
    ref = filter(lambda x: x != '' and x != '…' and x != '！' and x != '？' and x != '，' and x != '。' and x != '、', ref)
    # print hyp, ref
    # for h in hyp:
    #     print "tt"+h+"tt"
    # for r in ref:
    #     print "tt"+r+"tt"
    BLEUscore = nltk.translate.bleu_score.sentence_bleu([ref], hyp)
    print BLEUscore

hypothesis = ['It', 'is', 'a', 'cat', 'at', 'room']
reference = ['It', 'is', 'a', 'cat', 'inside', 'the', 'room']

hypothesis = ['我', '是', '一', '只', '猫']
reference = ['不', '好', '一']
# reference = ['我', '是', '一', '只', '狗']
#there may be several references


hypothesis = ['在',  '社交' , '网络',  '面前',  '人人' , '都' , '是',  '社交',  '网络',  '。']
reference = ['咫尺',  '天涯',  '，',  '有',  '没',  '有',  '/']
print hypothesis, reference

# for h in hypothesis:
#     print "tt"+h+"tt"
# for r in reference:
#     print "tt"+r+"tt"
BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis, )
print BLEUscore