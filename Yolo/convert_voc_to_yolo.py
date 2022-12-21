# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:44:21 2022

@author: Mai Van Hoa - HUST
"""

import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join


LIST_CLASSES = ['Chuỗi néo dây cáp quang',
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
				'Hư hỏng - Tạ chống rung - Gãy']

# def get_list_cls(path):
#     list_cls = []
#     file_names = glob.glob(path+'/*.xml')
    
#     for file_name in file_names:
#         file = open(file_name, encoding="utf8")
#         tree = ET.parse(file)
#         root = tree.getroot()
#         for obj in root.iter('object'):
#             cls = obj.find('name').text
#             if cls not in list_cls:
#                 list_cls.append(cls)
    
#     print(list_cls)
#     return list_cls


def convert(size, box): # size = (w, h), box = (xmin, xmax, ymin, ymax)
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(path_voc, path_yolo):
    # list_cls = get_list_cls(path_voc)
    list_cls = LIST_CLASSES
    class_file = open(path_yolo + '/classes.txt', 'w', encoding="utf8")
    for cls in list_cls:
        class_file.write(cls + '\n')
    
    file_names = glob.glob(path_voc +'/*.xml')
    
    for file_name in file_names:
        basename = os.path.basename(file_name)
        basename_no_ext = os.path.splitext(basename)[0]
        
        in_file = open(file_name, encoding="utf8")
        out_file = open(path_yolo + '/' + basename_no_ext + '.txt', 'w')
        
        
        tree = ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        for obj in root.iter('object'):
            cls = obj.find('name').text

            if cls in LIST_CLASSES:
                cls_id = list_cls.index(cls)
                
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                bb = convert((w,h), b)
                out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


def move_index_label(path_yolo, path_save):
    file_names = glob.glob(path_yolo +'/*.txt')

    for file_name in file_names:
        basename = os.path.basename(file_name)
        basename_no_ext = os.path.splitext(basename)[0]
        
        if basename != 'classes.txt':
        
            in_file = open(file_name)
            out_file = open(path_save + '/' + basename_no_ext + '.txt', 'w')
            
            lines = in_file.read()
    
            if len(lines):
                lines = lines.split('\n')
                
                for line in lines:
                    if len(line):
                        arr = line.split()
                        if int(arr[0]) >= 2:
                            arr[0] = str(int(arr[0]) - 2)
                            
                        out_file.write(" ".join(arr) + '\n')



if __name__ == '__main__':
    path_voc = r'C:\Users\DELL\Desktop\Label_YOLO\data_Kon\labels\voc'
    path_yolo = r'C:\Users\DELL\Desktop\Label_YOLO\data_Kon\labels\yolo'
    # path_save = r'C:\Users\DELL\Desktop\Label_YOLO\all_data\all_data\labels_move')
    
    if not os.path.exists(path_yolo):
        os.makedirs(path_yolo)
        
    # get_list_cls(path_voc)
    convert_annotation(path_voc, path_yolo)
    # move_index_label(path_yolo, path_save)
    
    
    
    
    