from ultralytics import YOLO
import cv2
import numpy as np
from ultralytics.utils.plotting import Annotator


def train_the_model():
    # Load a model
    model = YOLO()  # build a new model from scratch
    # model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    # it will save the best.pt modulw in runs/weight/best.pt
    model.train(
        data=r"data.yaml", # This is your yaml after creating data using roboflow
        epochs=100,
    )  # train the model
    
    metrics = model.val()  # evaluate model performance on the validation set
    results = model(r"D:\Fruits-detection\train\images\0a2bfef3b22f77b6_jpg.rf.1a02b2e598332c6a99dda6d89eda1f9c.jpg", retina_masks=True)  # predict on an image

    print(results)

# train_the_model()
    
def test_the_model(img, model):
    
    image = cv2.imread(img,1)
   
    results = model.predict(
        image,
        
    )
    for r in results:
        
        annotator = Annotator(image)
        
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
          
    img = annotator.result()  
    cv2.imshow('YOLO V8 Detection', img)     
    cv2.waitKey(0) & 0xFF == ord('q')
        
    
    
    

    # cv2.imshow("image", image)
    
    # cv2.waitKey(0)

import glob 
images =glob.glob(r"D:\Fruits-detection\valid\images\*.jpg")
model = YOLO(r"D:\Fruits-detection\runs\detect\train6\weights\best.pt")

for img in images:
    test_the_model(img,model)
