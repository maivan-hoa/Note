# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:45:27 2022

@author: Mai Van Hoa - HUST
"""
import glob
import os
import matplotlib.pyplot as plt
from collections import defaultdict

CLASSES = ['Chuỗi néo dây cáp quang',
            'Móng cột',
            'Chuỗi néo dây chống sét',
            'Chuỗi đỡ dây cáp quang',
            'Chuỗi đỡ dây chống sét',
            'Hư hỏng - Biển báo - Rỉ sét',
            'Chuỗi cách điện kép Composite',
            'Chuỗi cách điện đơn Composite',
            'Chuỗi cách điện đơn',
            'Chuỗi cách điện kép',
            'Hư hỏng - Chuỗi cách điện - Vỡ',
            'Hư hỏng - Vật lạ bám (diều, bạt)',
				'Hư hỏng - Đèn - Vỡ',
				'Hư hỏng - Dây - Phóng điện',
				'Hư hỏng - Dây - Tưa, đứt sợi',
				'Hư hỏng - Chuỗi cách điện - Phóng điện',
				'Hư hỏng - Chuỗi cách điện composite - Rách tán',
				'Hư hỏng - Sừng phóng điện - Gãy, cong',
				'Hư hỏng - Tạ chống rung - Gãy',
            'Hư hỏng - Khung định vị - Gãy']


path_label = './data_bad/data_0/labels'

list_labels = glob.glob(path_label + '/*.txt')
list_labels = [l for l in list_labels if 'classes.txt' not in l]

d = defaultdict(int)

for label in list_labels:
    with open(label, 'r') as f:
        data = f.read()
        data = data.split('\n')
        data = [d for d in data if d]
        data = [int(i.split()[0]) for i in data]
        
        for i in data:
            d[i] += 1

print('Tổng số ảnh: ', len(list_labels))
for k, v in d.items():
    print('{}: {}'.format(CLASSES[k], v))

















