import torch
import numpy as np
import glob
import os
from PIL import Image

def inference_yolo(root_yolo, path_model, path_image, path_save_label, device='0', img_size=640, conf=0.25, iou=0.45, append=True):
    model = torch.hub.load(root_yolo, 'custom', path=path_model, source='local', device=device)  # local repo, ./ là đường dẫn đến thư mục chứa mã nguồn yolo
    model.conf = conf
    model.iou = iou
    
    list_path_img = glob.glob(path_image + '/*')
    for path in list_path_img:
        img = Image.open(path)
        W, H = img.size
        results = model(img, size=img_size)

        arr = results.xyxy[0].cpu().numpy()[:, [5, 0, 1, 2, 3]]

        center_x = (arr[:, 1] + arr[:, 3])/2
        center_y = (arr[:, 2] + arr[:, 4])/2
        width = arr[:, 3] - arr[:, 1]
        height = arr[:, 4] - arr[:, 2]

        arr[:, 1] = center_x / W
        arr[:, 2] = center_y / H
        arr[:, 3] = width / W
        arr[:, 4] = height / H

        basename = os.path.basename(path)
        basename_no_ext = os.path.splitext(basename)[0]

        with open(path_save_label + '/' + basename_no_ext + '.txt', 'a+') as f:
            for box in arr:
                line = box.tolist()
                line[0] = int(line[0])
                line = [str(i) for i in line]
                line = ' '.join(line) + '\n'
                f.write(line)
                
    print('Done!')


if __name__ == '__main__':
    root_yolo = './yolov5'
    path_model = './yolov5/runs/train/exp7/weights/best.pt'
    path_image = './data/image'
    path_save_label = './data/label'

    inference_yolo(root_yolo, path_model, path_image, path_save_label)