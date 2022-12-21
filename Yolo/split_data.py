import os
import numpy as np
import glob
import math
import shutil
from random import sample

def spilt_folder():
    root = './test_code'
    
    number_image_each_folder = 1
    path_image = os.path.join(root, 'data/images')
    path_label = os.path.join(root, 'data/labels')
    
    list_images = glob.glob(path_image + '/*')
    list_labels = [i.replace('images', 'labels').replace('jpg', 'txt') for i in list_images]
    
    number_images = len(list_images)
    number_folder = math.ceil(number_images / number_image_each_folder)
    
    list_images.sort()
    list_labels.sort()
    
    for path in list_labels:
        with open(path, 'a+') as f:
            continue
    
    if not os.path.exists(os.path.join(root, 'split_data')):
        os.mkdir(os.path.join(root, 'split_data'))
            
    
    for i in range(number_folder):
        if not os.path.exists(os.path.join(root, 'split_data', 'data_{}'.format(i))):
            os.makedirs(os.path.join(root, 'split_data', 'data_{}'.format(i), 'images'))
            os.makedirs(os.path.join(root, 'split_data', 'data_{}'.format(i), 'labels'))
        
        start = i*number_image_each_folder
        stop = min(start + number_image_each_folder, number_images)
        for j in range(start, stop):
            shutil.copy2(list_images[j], os.path.join(root, 'split_data', 'data_{}'.format(i), 'images'))
            shutil.copy2(list_labels[j], os.path.join(root, 'split_data', 'data_{}'.format(i), 'labels'))


def split_train_test_val():
    root = './data_evn'
    
    path_image = os.path.join(root, 'data_clean/images')
    path_label = os.path.join(root, 'data_clean/labels')
    
    path_train = os.path.join(root, 'train')
    path_val = os.path.join(root, 'valid')
    
    if not os.path.exists(path_train):
        os.makedirs(os.path.join(path_train, 'images'))
        os.makedirs(os.path.join(path_train, 'labels'))
        
    if not os.path.exists(path_val):
        os.makedirs(os.path.join(path_val, 'images'))
        os.makedirs(os.path.join(path_val, 'labels'))
    
    list_images = glob.glob(path_image + '/*')
    list_labels = glob.glob(path_label + '/*')
    list_labels = [l for l in list_labels if 'classes.txt' not in l]
    
    list_images.sort()
    list_labels.sort()
    
    n = len(list_images)
    list_index = range(n)
    
    list_index_val = sample(list_index, int(0.2*n))
    list_index_train = list(set(list_index) - set(list_index_val))
    
    for i in list_index_train:
        shutil.move(list_images[i], list_images[i].replace('data_clean', 'train'))
        shutil.move(list_labels[i], list_labels[i].replace('data_clean', 'train'))
        
    for i in list_index_val:
        shutil.move(list_images[i], list_images[i].replace('data_clean', 'valid'))
        shutil.move(list_labels[i], list_labels[i].replace('data_clean', 'valid'))
        

if __name__ == '__main__':
    split_train_test_val()























