# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:44:06 2022

@author: Mai Van Hoa - HUST
"""
import glob
import os


path_images = './data_bad/data_0_0/images'
path_labels = './data_bad/data_0_0/labels'

list_labels = glob.glob(path_labels + '/*.txt')
list_labels = [l for l in list_labels if 'classes.txt' not in l]
list_images = glob.glob(path_images + '/*')

list_labels.sort()
list_images.sort()

for i, label in enumerate(list_labels):
    with open(label, 'r') as f:
        data = f.read()
        
    if not data:
        os.remove(label)
        os.remove(list_images[i])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        