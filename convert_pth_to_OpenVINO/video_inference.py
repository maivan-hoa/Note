# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:48:33 2021

@author: Mai Van Hoa - HUST
"""

from imports import *
from model_inference import *
from architecture import *
from imutils.video import FPS

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

CLASSES = {
    0: 'Bien',
    1: 'Cuong',
    2: 'LeDong',
    3: 'Phu',
    4: 'Vu',
    5: 'Nguyen',
    6: 'Hoa'
}

class Model_classification():
    def __init__(self, model_xml, model_bin):
        self.model_xml = model_xml
        self.model_bin = model_bin
        ie = IECore()
        net =  ie.read_network(model=model_xml, weights=model_bin)
        self.input_blob = next(iter(net.input_info))
        self.out_blob = next(iter(net.outputs))
        self.exec_net =  ie.load_network(network=net, device_name="CPU")
        
        
    def predict(self, input):
        result_vector = self.exec_net.infer(inputs={self.input_blob: input})
        result_vector = result_vector[self.out_blob]
        return result_vector[0]
    
    
class Model_detector():
    def __init__(self, model_xml, model_bin):
        self.model_xml = model_xml
        self.model_bin = model_bin
        ie = IECore()
        net =  ie.read_network(model=model_xml, weights=model_bin)
        self.input_blob = next(iter(net.input_info))
        self.out_blob = next(iter(net.outputs))
        self.exec_net =  ie.load_network(network=net, device_name="CPU")
        self.n, self.c, self.h, self.w = net.input_info[self.input_blob].input_data.shape
        
    
    def predict(self, input, conf=0.5):
        h_origin, w_origin, _ = input.shape
        corr_faces = []
        input = cv2.resize(input, (self.w, self.h))
        input = input.transpose((2, 0, 1))
        input = input[np.newaxis, ...]
        results = self.exec_net.infer(inputs={self.input_blob: input})
        results = results[self.out_blob]
        
        for res in results[0, 0]:
            if res[2] > conf:
                # kết quả là tỷ lệ tọa độ khung hình đầu vào
                x_min = max(res[3], 0)
                y_min = max(res[4], 0)
                x_max = max(res[5], 0)
                y_max = max(res[6], 0)
                
                # convert sang tọa độ của ảnh gốc ban đầu
                x1 = int(x_min * w_origin)
                y1 = int(y_min * h_origin)
                x2 = int(x_max * w_origin)
                y2 = int(y_max * h_origin)
                corr_faces.append((x1, y1, x2, y2))
        return corr_faces
    


imgGlass = cv2.imread('./data/glasses_mask.png', 0)
r = 160 / imgGlass.shape[1]
dim = (160, int(imgGlass.shape[0] * r))
imgGlass = cv2.resize(imgGlass, dim, interpolation = cv2.INTER_AREA)
imgGlass = imgGlass[39:81, 21:138]

# height và width ban đầu của kính
origGlassHeight, origGlassWidth = imgGlass.shape[:2]

imgGlass[imgGlass < 50] = 0
imgGlass[imgGlass >= 50] = 255
# plt.imshow(imgGlass)

# Tạo mask là mảng nhị phân hai chiều
mask_Glass = imgGlass/255 # kính trắng, nền đen


def predict_class_face(face, model_clf, required_size=(112, 112)):
    
    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    # resize face to the model size
    face = cv2.resize(face, required_size)
    
    face = np.asarray([face], dtype='float16')
    # prepare the face for the model
    face = face.transpose((0, 3, 1, 2))
    face = (face - 127.5) / 128
    
    # perform prediction
    yhat = model_clf.predict(face)
    softmax = nn.Softmax(dim=0)
    prob = softmax(torch.Tensor(yhat))
        
    cl = np.argmax(prob).item()
    
    return CLASSES[cl], prob[cl].numpy()#, prob[0].numpy()


def affix_glass(image, glass_fake, predict_landmark, drect):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # detect landmarks
    shapes = predict_landmark(image, drect)
    
    # Tìm height và width của kính trong ảnh khuôn mặt
    glassWidth = shapes.part(16).x - shapes.part(0).x
    glassHeight = int(glassWidth * origGlassHeight / origGlassWidth)
    
    # tìm vùng để đặt kính
    y1 = int(shapes.part(22).y)
    y2 = int(y1 + glassHeight)
    x1 = int(shapes.part(27).x - glassWidth/2)
    x2 = x1 + glassWidth
    
    # Xử lý khi tọa độ các landmark vượt ra ngoài kích thước khung ảnh
    if y1 < 0:
        y1 = 0
        glassHeight -= abs(y1)
    if x1 < 0:
        glassWidth -= abs(x1)
        x1 = 0
    if x2 > image.shape[1]:
        glassWidth -= (x2 - image.shape[1])
        x2 = image.shape[1]
        
    glass = cv2.resize(glass_fake, (glassWidth, glassHeight))
    mask = cv2.resize(mask_Glass, (glassWidth, glassHeight))
    mask = np.stack((mask,)*3, -1)
    
    image = image/255
    roi = image[y1:y2, x1:x2]
    roi = roi - mask
    roi = np.clip(roi, 0, 1)
    image[y1:y2, x1:x2] = glass + roi 
    
    image = (image*255).astype('uint8')
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # (image*255).astype('uint8')


def run(path_netG, model_clf, model_detector, predict_landmark, required_size=(112, 112), save_video=False):
    
    # Kính để test
    # glass = io.imread("./data/eyeglasses/glasses000002-2.png")
    # glass = cv2.resize(glass, (160, 160), interpolation = cv2.INTER_AREA)
    # plt.imshow(glass)
    # glass = glass/255
    # # glass = np.transpose(glass, (2, 0, 1))
    # glass = glass[39:81, 21:138]
    
    if path_netG != None:
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        nc, ndf, ngf, nz = 3, 160, 160, 100
    
        netG = Generator(nc=nc, ngf=ngf, nz=nz).to(device)
        netG.load_state_dict(torch.load(path_netG, map_location=device))
        
        netG.eval()
        
        with torch.no_grad():
            noise = torch.randn(1, 100, 1, 1, device=device)
            fix_noised = noise
            glass = netG(noise)
        
        glass = normalize_glass(glass)
        glass = glass[0].permute(1,2,0)
        glass = glass.numpy()
        glass = cv2.resize(glass, (160, 160), interpolation = cv2.INTER_AREA)
        
        glass = glass[39:81, 21:138]
        glass[mask_Glass == 0] = 0
        # plt.imshow(glass)
    
    
    camera = cv2.VideoCapture(0)
    # camera = cv2.VideoCapture('./data/cam_test.avi')
    
    if save_video == True:
        frame_width = int(camera.get(3))
        frame_height = int(camera.get(4))
        size = (frame_width, frame_height)
        
        # Parameters:
        # filename: Input video file
        # fourcc: 4-character code of codec used to compress the frames
        # fps: framerate of videostream
        # framesize: Height and width of frame
        writer = cv2.VideoWriter('./data/Have_glass.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
        
    fps = FPS().start()
    
    while True:
        success, image = camera.read()

        corr_faces = model_detector.predict(image)
        for corr in corr_faces:
            # left, top, right, bottom
            x1, y1, x2, y2 = corr
            drect = dlib.rectangle(x1, y1, x2, y2)
            
            
            # for i in range(68):
            #     x, y = shapes.part(i).x, shapes.part(i).y
            #     cv2.circle(image, (x, y), 1, (0, 225, 0), -1)
            
            if path_netG != None:
                image = affix_glass(image, glass, predict_landmark, drect)
            # classification face
            face = image[y1:y2, x1:x2]
            predicted, prob = predict_class_face(face, model_clf)
            
            
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, predicted, (x1, y1-25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)
            cv2.putText(image, str(np.round(prob, 2)), (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)        
            
        if save_video == True:
            writer.write(image)
            
        cv2.imshow('frame', image)
        fps.update()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    fps.stop()
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    camera.release()
    cv2.destroyAllWindows()
    
    

if __name__ == '__main__':
    required_size=(112, 112)
    
    netG = './model/netG_backup.pth'
    
    model_clf_xml = './model/MobileFaceNet_classification.xml'
    model_clf_bin = './model/MobileFaceNet_classification.bin'
    model_clf = Model_classification(model_clf_xml, model_clf_bin)
    
    # Yêu cầu hệ màu đầu vào là BGR
    model_detector_xml = './model/face-detection-0204_fp16.xml'
    model_detector_bin = './model/face-detection-0204_fp16.bin'
    model_detector = Model_detector(model_detector_xml, model_detector_bin)
    
    predict_landmark = dlib.shape_predictor('./model/shape_predictor_68_face_landmarks.dat')
    
    # run(netG, model_clf, model_detector, predict_landmark, save_video=False)
    run(None, model_clf, model_detector, predict_landmark, save_video=False)














