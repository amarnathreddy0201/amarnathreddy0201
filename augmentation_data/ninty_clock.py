import cv2
import numpy as np

def rotate_bounding_box_90_counter_clockwise(bboxes, img_width):
    """
    Rotates bounding boxes 90 degrees clockwise.

    Parameters:
    bboxes (list of tuples): List of (xmin, ymin, xmax, ymax) coordinates of the bounding boxes.
    img_width (int): Width of the original image.

    Returns:
    list of tuples: New list of (xmin, ymin, xmax, ymax) coordinates after rotation.
    """
    rotated_bboxes = []
    for (xmin, ymin, xmax, ymax) in bboxes:
        new_xmin = ymin
        new_ymin = img_width - xmax
        new_xmax = ymax
        new_ymax = img_width - xmin

        # Ensuring that new coordinates are correctly ordered
        new_xmin, new_xmax = min(new_xmin, new_xmax), max(new_xmin, new_xmax)
        new_ymin, new_ymax = min(new_ymin, new_ymax), max(new_ymin, new_ymax)

        rotated_bboxes.append((new_xmin, new_ymin, new_xmax, new_ymax))
    return rotated_bboxes

def rotate_bounding_box_90_clockwise(bboxes, img_width):
    """
    Rotates bounding boxes 90 degrees clockwise.

    Parameters:
    bboxes (list of tuples): List of (xmin, ymin, xmax, ymax) coordinates of the bounding boxes.
    img_width (int): Width of the original image.

    Returns:
    list of tuples: New list of (xmin, ymin, xmax, ymax) coordinates after rotation.
    """
    rotated_bboxes = []
    for (xmin, ymin, xmax, ymax) in bboxes:
        new_xmin = img_width - ymax
        new_ymin = xmin
        new_xmax = img_width - ymin
        new_ymax = xmax

        # new_xmin = img_width - ymax
        # new_ymin = xmin
        # new_xmax = img_width - ymin
        # new_ymax = xmax

        # Ensuring that new coordinates are correctly ordered
        new_xmin, new_xmax = min(new_xmin, new_xmax), max(new_xmin, new_xmax)
        new_ymin, new_ymax = min(new_ymin, new_ymax), max(new_ymin, new_ymax)

        rotated_bboxes.append((new_xmin, new_ymin, new_xmax, new_ymax))
    return rotated_bboxes

import os
import glob
names = ['drone'] # Your classes
images = glob.glob(r"D:\AMAR_Gitwork\drone_detection\drone_dataset_yolo\dataset_txt\*.jpg") # Images directory
# print(images)

labels_folder = r"D:\AMAR_Gitwork\drone_detection\drone_dataset_yolo\dataset_txt" # Label directory
import cv2
for image in images:

    image_read = cv2.imread(image,1)
    ninty_counter_clock = cv2.rotate(image_read, cv2.ROTATE_90_COUNTERCLOCKWISE) # Rotate the image 90 degrees clockwise()
    ninty_clock = cv2.rotate(image_read, cv2.ROTATE_90_CLOCKWISE)
    h,w,_ = image_read.shape

    image_name = image.split("\\")[-1] # Get image name

    image_name = image_name[:image_name.find(".jpg")] # Remove .jpg
    print(image_name)

    original_bboxes = []

    with open(os.path.join(labels_folder, image_name + ".txt")) as f: # Checking the labels txt files
        read_lines = f.readlines() # read all lines of labels
        # print(read_lines)

        # line = read_lines.split("\n")
        # print(line)
        for line in read_lines: # Read each line
            # Remove \n at the endd of the labels
            # Split by space 

            clss , x1, y1, x2, y2 = map(float,line.replace("\n", "").split(" "))
            
            clas = names[int(clss)] # Get class

            # class_id = int(line[0])
            x_center_norm = float(x1) # Normalize the coordinates
            y_center_norm = float(y1)
            width_norm = float(x2)
            height_norm = float(y2)


            x_center = int(x_center_norm * w) # Convert to int and making with bounding boxes properly
            y_center = int(y_center_norm * h)
            box_width = int(width_norm * w)
            box_height = int(height_norm * h)

            # Calculate the top-left and bottom-right corners of the rectangle
            x1 = x_center - box_width // 2 
            y1 = y_center - box_height // 2
            x2 = x_center + box_width // 2
            y2 = y_center + box_height // 2

            original_bboxes.append((x1, y1, x2, y2))

            cv2.rectangle(image_read, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image_read, clas, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        
        

        bboxes = rotate_bounding_box_90_clockwise(original_bboxes, w)

        for (xmin, ymin, xmax, ymax) in bboxes:
            cv2.rectangle(ninty_clock, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)


        image_read = cv2.resize(image_read, (640, 480))
        ninty_clock = cv2.resize(ninty_clock, (640, 480))
        ninty_counter_clock = cv2.resize(ninty_counter_clock, (640, 480))
    cv2.imshow("image", image_read)
    cv2.imshow("ninty_clock", ninty_clock)
    
    cv2.waitKey(0)
            

        
        

