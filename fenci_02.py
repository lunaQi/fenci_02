# !/usr/bin/env python
# -*- coding : utf-8 -*-
import jieba
import jieba.posseg as pseg

def delete_space(stopwordspath):

    stw_list = [line.strip()
                for line in open(stopwordspath,'r')]
    return stw_list

f1 = open("150518it23974.txt")
f2 = open("fenci_150518it23974.txt",'a')

lines = f1.readlines()
'''
for line in lines:
    print line.decode('utf-8')
'''
text = ''


for line in lines:
    line.replace('\t','').replace('\n','').replace(' ','')
    #seg_list = jieba.cut(line, cut_all=False)
    words = pseg.cut(line)
    #for word in seg_list:
    for word, flag in words:
        if (flag == 'Ng') or (flag=='n') or (flag=='nr') or (flag=='ns') or (flag=='nt') or (flag=='nz') or (flag=='vn'):
            text = text + '\n'+ str(word.encode('utf8')) + ' ' + str(flag)

print(text)

f2.write(text)

f1.close()
f2.close()
