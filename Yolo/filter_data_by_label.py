# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:45:53 2022

@author: Mai Van Hoa - HUST
"""
import glob
import os
import shutil

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


root_origin = './data_bad/data_2'
root_filter = './data_bad/filter_image'

class_filter = ['Hư hỏng - Dây - Tưa, đứt sợi',
                'Hư hỏng - Vật lạ bám (diều, bạt)',
                'Hư hỏng - Tạ chống rung - Gãy',
                'Hư hỏng - Biển báo - Rỉ sét',
                'Hư hỏng - Khung định vị - Gãy',
                'Hư hỏng - Đèn - Vỡ',
                'Hư hỏng - Dây - Phóng điện',
                'Hư hỏng - Chuỗi cách điện composite - Rách tán',
                'Hư hỏng - Chuỗi cách điện - Phóng điện',
                'Hư hỏng - Sừng phóng điện - Gãy, cong'
                ]
index_class_filter = []

for c in class_filter:
    index_class_filter.append(CLASSES.index(c))


list_labels = glob.glob(os.path.join(root_origin, 'labels') + '/*.txt')
list_labels = [l for l in list_labels if 'classes.txt' not in l]
list_images = glob.glob(os.path.join(root_origin, 'images') + '/*')

list_labels.sort()
list_images.sort()

for i, label in enumerate(list_labels):
    with open(label, 'r') as f:
        data = f.read()
        data = data.split('\n')
        data = [d for d in data if d]
        data = [int(i.split()[0]) for i in data]
        
    intersection = set.intersection(set(index_class_filter), set(data))
    if intersection:
        if not os.path.exists(os.path.join(root_filter, 'images')):
            os.makedirs(os.path.join(root_filter, 'images'))
            os.makedirs(os.path.join(root_filter, 'labels'))

        shutil.copy2(list_images[i], os.path.join(root_filter, 'images'))
        shutil.copy2(list_labels[i], os.path.join(root_filter, 'labels'))
























































