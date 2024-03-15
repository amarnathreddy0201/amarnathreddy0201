from ultralytics import YOLO
import cv2


model = YOLO(r"C:\Development\multi_class\numberwise_class.pt")
results = model(source=r"C:\Users\alluv\Downloads\snapshot_2024_01_25_23_04_29.jpg")

image = cv2.imread(r"C:\Users\alluv\Downloads\snapshot_2024_01_25_23_04_29.jpg", 1)

for d in results[0].boxes:
    cls = d.cls.int
    conf = d.conf
    x1, y1, x2, y2 = d.xyxy[0]
    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(
        image,
        str(cls),
        (int(x1), int(y1) - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
    )

cv2.imshow("image", image)
cv2.waitKey(0)



##################################################################################################################

# Prediction of yolov7 with numbers


# import torch
# import cv2
# from models.yolo import Model  # Import YOLOv7 model class
# from utils.general import non_max_suppression, scale_coords


# model = torch.hub.load("yolov7", "custom", path=r"C:\Amar_Development\yolov7\runs\train\yolov74\weights\best.pt", device="0")

# !# Download YOLOv7 code
# !git clone https://github.com/WongKinYiu/yolov7
# %cd yolov7
from pathlib import Path

import torch
import cv2

from models.yolo import Model
from utils.general import check_requirements, set_logging
from utils.google_utils import attempt_download
from utils.torch_utils import select_device

dependencies = ['torch', 'yaml']
check_requirements(Path("/content/yolov7/").parent / 'requirements.txt', exclude=('pycocotools', 'thop'))
set_logging()

def custom(path_or_model='path/to/model.pt', autoshape=True):
    """custom mode

    Arguments (3 options):
        path_or_model (str): 'path/to/model.pt'
        path_or_model (dict): torch.load('path/to/model.pt')
        path_or_model (nn.Module): torch.load('path/to/model.pt')['model']

    Returns:
        pytorch model
    """
    model = torch.load(path_or_model, map_location=torch.device('cpu')) if isinstance(path_or_model, str) else path_or_model  # load checkpoint
    if isinstance(model, dict):
        model = model['ema' if model.get('ema') else 'model']  # load model

    hub_model = Model(model.yaml).to(next(model.parameters()).device)  # create
    hub_model.load_state_dict(model.float().state_dict())  # load state_dict
    hub_model.names = model.names  # class names
    if autoshape:
        hub_model = hub_model.autoshape()  # for file/URI/PIL/cv2/np inputs and NMS
    device = select_device('0' if torch.cuda.is_available() else 'cpu')  # default to GPU if available
    return hub_model.to(device)

model = custom(path_or_model=r"C:\Amar_Development\yolov7\runs\train\yolov74\weights\best.pt")  # custom example
# model = create(name='yolov7', pretrained=True, channels=3, classes=80, autoshape=True)  # pretrained example

# Verify inference
import numpy as np
from PIL import Image

imgs = cv2.imread(r"C:\Amar_Development\pipe-detection-1\test\images\snapshot_112_jpg.rf.619720fe019e2a6c28691f35ca682fc9.jpg",1)

results = model(imgs)  # batched inference


pred = results.pandas().xyxy[0]

# Plot each bounding box
for index, row in pred.iterrows():
    xmin, ymin, xmax, ymax,conf,clss, name = row['xmin'], row['ymin'], row['xmax'], row['ymax'],row["confidence"],row["class"],row["name"]

    cv2.circle(imgs, (int((row["xmin"] + row["xmax"]) * 0.5), int((row["ymin"] + row["ymax"]) * 0.5)),
                   int((row["xmax"] - row["xmin"]) * 0.5 * 0.6), (255, 0, 0), -1)
    

    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 

    # Calculate center points
    center_x = int((xmin + xmax) / 2)
    center_y = int((ymin + ymax) / 2)
    
    # org 
    org = (center_x, center_y) 
    
    # fontScale 
    fontScale = 1
    
    # Blue color in BGR 
    color = (0, 0, 255) 
    
    # Line thickness of 2 px 
    thickness = 2

    # Using cv2.putText() method 
    cv2.putText(imgs, name, org, font,  fontScale, color, thickness, cv2.LINE_AA) 

cv2.imshow("image",imgs)
cv2.waitKey(0)
