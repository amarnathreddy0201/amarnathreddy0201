from ultralytics import YOLO
import glob
import os
import cv2
from datetime import datetime
import json
import re
images = glob.glob("test/images/*.jpg")
images.extend(glob.glob("test/images/*.jpeg"))
images.sort()

labels_directory = "test/labels"
gt_labels ={}
pt_labels={}
labels = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle',"None"]
map_label ={"Hardhat":"Helmet","NO-Hardhat":"No_helmet","Safety Vest":"Vest","NO-Safety Vest":"No_vest","Person":"Person"}
kag_ori_label=[
    'Helmet', 
    'Gloves', 
    'Vest', 
    'Boots', 
    'Googles', 
    'No_vest', 
    'Person', 
    'No_helmet', 
    'No_googles', 
    'No_gloves', 
    'No_boots'
]
map_orig_lab ={0:0,2:7,7:2,4:5,5:6}
categories = [
    {"supercategory": "Hel", "id": 0, "name": "Hel"},
    {"supercategory": "Vest", "id": 2, "name": "Vest"},
    {"supercategory": "Pers", "id": 6, "name": "Pers"}
]
# Lists to store data
images = []
annotations = []
licenses = [{"id": 1, "name": "Unknown", "url": ""}]
annotation_id = 1
ground_prediction_directory = "ground_prediction_directory"
os.makedirs(ground_prediction_directory, exist_ok=True)
def read_file(label_path):
    labels_orig = []
    with open(label_path, 'r') as label_file:
        labels = label_file.readlines()
        # Loop through each label
        for label in labels:
            class_id, x_center, y_center, width, height = map(float, label.split())
            labels_orig.append(int(class_id))
    return labels_orig


def extract_numbers(filename):
    match = re.search(r'\d+', filename)  # Find the first sequence of digits
    return match.group() if match else None  # Return the number if found, else None


model = YOLO("yolov8x.pt")

count =0
total_person =0
print("total no of images : " , len(images))
collect_data =[]

images_directory = 'test/images'  # Replace with the correct path to your images
labels_directory = 'test/labels' 

# Iterate over the files in the images directory
for filename in os.listdir(images_directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):

        image_path = os.path.join(images_directory, filename)

        name, ext = os.path.splitext(filename)
        if ext.lower() in {'.jpg', '.jpeg', '.png'}:
            label_path = os.path.join(labels_directory, name + '.txt')

        image_id = extract_numbers(filename)

        original_image = cv2.imread(image_path,1)
        width, height, _ = original_image.shape

        images.append({
            "id": image_id,
            "width": width,
            "height": height,
            "file_name": filename,
            "license": 1,
            "flickr_url": "",
            "coco_url": "",
            "date_captured": datetime.now().isoformat(),
        })

        results = model(original_image)
        for res in results:
            for data in res.boxes:
                category_id = int(data.cls[0])  # Numeric class ID

                x_center_rel, y_center_rel, width_rel, height_rel = data.xywh[0]
                if category_id in [0,  5,  7]:
                    
                    score = data.conf[0].item()
                    # Convert from relative to absolute coordinates
                    x_center_abs = x_center_rel.item() 
                    y_center_abs = y_center_rel.item() 
                    box_width_abs = width_rel.item() 
                    box_height_abs = height_rel.item()

                    original_index = map_orig_lab[category_id]

                    cv2.rectangle(original_image, (int(x_center_abs-box_width_abs//2), int(y_center_abs-box_height_abs//2)), 
                                  (int(x_center_abs+box_width_abs//2), int(y_center_abs+box_height_abs//2)), (0, 255, 0), 2)

                    cv2.putText(original_image, (kag_ori_label[original_index]), (int(x_center_abs-box_width_abs//2), int(y_center_abs-box_height_abs//2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
                    
                    annotations.append({
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": int(original_index),
                        "segmentation": [],
                        "area": box_width_abs * box_height_abs,
                        "bbox": [x_center_abs, y_center_abs, box_width_abs, box_height_abs],
                        "iscrowd": 0,
                        "score": score
                    })
                    annotation_id += 1
                    
                    class_name = res.names[category_id]

        cv2.imwrite(ground_prediction_directory +"/"+filename, original_image)

# COCO format structure
# coco_format = {
    
#     images
# }

# Write to JSON file
output_json_path = 'predicting.json'
with open(output_json_path, 'w') as file:
    json.dump(annotations, file, indent=4)