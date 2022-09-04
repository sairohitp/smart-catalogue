from sre_constants import SUCCESS
import cv2 as cv
import numpy as np
import matplotlib as mat

cap = cv.VideoCapture(0)

confThreshold = 0.5

classesFile = 'coco.names'
with open(classesFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)
print(len(classNames))

modelConfiguration = "C:/Users/tarun/Documents/Projects/OpenCV/yolov3-coco/yolovo3.cfg"
modelWeight = 'C:/Users/tarun/Documents/Projects/OpenCV/yolov3-coco/yolovo3.weights'

net = cv.dnn.readNetFromDarkNet(modelConfiguration,modelWeight)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

def findObjects(outputs,img):
    ht,wt,ct = img.shape
    bbox = []
    classIds = []
    confs = []
    for output in outputs:
        for det in output:
             scores = det[5:]
             classId = np.argmax(scores)
             confidence = scores[classId]
             if confidence > confThreshold :
                w,h = (det[2]* wt) , (det[3]*ht)
                x,y = int((det[0]*wt) - w/2),int((det[1]*ht)-h/2)
                bbox.append(classId)
                confs.append(float(confidence))


while True:
    SUCCESS, img = cap.read()
    blob = cv.dnn.blockFromImage(img,1/255,(320,320),[0,0,0],1,crop=False)
    net.setInput(blob)
    layerNames = net.getLayerNames()
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    output = net.forward(outputNames)
    print(len(output))
