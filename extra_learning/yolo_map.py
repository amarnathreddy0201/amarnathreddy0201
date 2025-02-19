import os
import json
from PIL import Image
from datetime import datetime
import re

def extract_numbers(filename):
    match = re.search(r'\d+', filename)  # Find the first sequence of digits
    return match.group() if match else None  # Return the number if found, else None

# categories = [
#     {"supercategory": "Helmet", "id": 0, "name": "Helmet"},
#     {"supercategory": "Vest", "id": 2, "name": "Vest"},
#     {"supercategory": "No_vest", "id": 5, "name": "No_vest"},
#     {"supercategory": "Person", "id": 6, "name": "Person"},
#     {"supercategory": "No_helmet", "id": 7, "name": "No_helmet"}
    
# ]

# labels = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle',"None"]
labels = ['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest',
              'Person', 'SUV', 'Safety Cone', 'Safety Vest', 'bus', 'dump truck', 'fire hydrant', 'machinery',
              'mini-van', 'sedan', 'semi', 'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']

categories = [
    {"supercategory": "Helmet", "id": 0, "name": "Helmet"},
    {"supercategory": "Gloves", "id": 1, "name": "Gloves"},
    {"supercategory": "No_helmet", "id": 7, "name": "No_helmet"},
    {"supercategory": "Vest", "id": 2, "name": "Vest"},
    {"supercategory": "No_vest", "id": 5, "name": "No_vest"},
    {"supercategory": "Person", "id": 6, "name": "Person"}
]

# Lists to store data
images = []
annotations = []
licenses = [{"id": 1, "name": "Unknown", "url": ""}]
annotation_id = 1


kaggle_original_labels=[
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


# for d in [0, 2, 5, 6, 7]:
#     print(kaggle_original_labels[d])

# Define directories
images_directory = 'images'  # Replace with the correct path to your images
labels_directory = 'labels'  # Replace with the correct path to your labels
import cv2
# Iterate over the files in the images directory
for filename in os.listdir(images_directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):

        image_path = os.path.join(images_directory, filename)

        original_image = cv2.imread(image_path,1)

        name, ext = os.path.splitext(filename)
        if ext.lower() in {'.jpg', '.jpeg', '.png'}:
            label_path = os.path.join(labels_directory, name + '.txt')

        print("image path ",image_path)
        print("label path ",label_path)
        # Extract numeric part from the filename and use it as the image ID
        # image_id = int(filename.split('.')[0].lstrip('0'))  # Remove leading zeros and file extension

        image_id = extract_numbers(filename)

        # Open the image to get width and height
        with Image.open(image_path) as img:
            width, height = img.size

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

        # Read the label file
        if os.path.exists(label_path):
            with open(label_path, 'r') as file:
                for line in file:
                    category_id, x_center_rel, y_center_rel, width_rel, height_rel = map(float, line.split())

                    x_cen = int(x_center_rel * width) 
                    y_cen = int(y_center_rel * height)
                    x_width = int(( width_rel) * width)
                    y_width = int(( height_rel) * height)

                    x1= int(x_cen-x_width//2)
                    y1= int(y_cen-y_width//2)
                    x2= int(x_cen+x_width//2)
                    y2= int(y_cen+y_width//2)
                    

                    
                    if category_id in [0,1, 2, 5, 6, 7]:
                        cv2.rectangle(original_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        
                        cv2.putText(original_image, f"Class {kaggle_original_labels[int(category_id)]} : {category_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                        
                        x_center_abs, y_center_abs = x_center_rel*width , y_center_rel *height
                        box_width_abs, box_height_abs = width_rel *width, height_rel *height

                        annotations.append({
                            "id": annotation_id,
                            "image_id": image_id,
                            "category_id": int(category_id),
                            "segmentation": [],
                            "area": box_width_abs * box_height_abs,
                            "bbox": [x_center_abs, y_center_abs, box_width_abs, box_height_abs],
                            "iscrowd": 0,
                        })
                        annotation_id += 1
        else:
            print(f"Label file not found for {filename}")

    # cv2.imshow("original_image ", original_image)
    # cv2.waitKey(0)

# COCO format structure
coco_format = {
    "info": {
        "year": 2024,
        "version": "1.0",
        "description": "Dataset description",
        "contributor": "Your name or organization",
        "url": "Dataset URL or your website",
        "date_created": datetime.now().isoformat()
    },
    "images": images,
    "annotations": annotations,
    "licenses": licenses,
    "categories": categories
}

# Write to JSON file
output_json_path = 'Algorithm1_amar_gt.json'
with open(output_json_path, 'w') as file:
    json.dump(coco_format, file, indent=4)

print(f"{output_json_path} has been created.")
