# !/usr/bin/env python
# -*- coding : utf-8 -*-
import jieba
import jieba.posseg as pseg

'''
def delete_space(stopwordspath):

    stw_list = [line.strip()
                for line in open(stopwordspath,'r')]
    return stw_list
'''

f1 = open("150518it23974.txt")
f2 = open("fenci_150518it23974.txt", 'w')

lines = f1.readlines()
'''
for line in lines:
    print line.decode('utf-8')
'''
text = ''


for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ', '')
    if len(line) > 0:      # delete a null line
        #seg_list = jieba.cut(line, cut_all=False)
        words = pseg.cut(line)

        #for word in seg_list:
        for word, flag in words:
            if (flag == 'Ng') or (flag == 'n') or (flag == 'nr') or (flag == 'ns') or (flag == 'nt') or (flag == 'nz') or (flag == 'vn'):
                text = text + ',' + str(word.encode('utf8'))

#print(text)

f2.write(text)

f1.close()
f2.close()

word_lst = []
word_dict = {}
with open("fenci_150518it23974.txt") as wf, open("wfr_150518it23974.txt", 'w') as wf2:
    for word in wf:
        word_lst.append(word.split(','))
        for item in word_lst:
            for item2 in item:
                if item2 not in word_dict:
                    word_dict[item2] = 1
                else:
                    word_dict[item2] += 1
    for key in word_dict:
        print key,str(word_dict[key])
        wf2.write(key + ' ' + str(word_dict[key]) + '\n')

