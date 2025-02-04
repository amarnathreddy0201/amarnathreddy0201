import os
import glob
from main import check_pleat

# names = ['damage', 'excess_glue', 'foreign_material', 'open_pleat']
names = ['open_pleat']

images = glob.glob(r"open_pleat_final_train_and_split\val\images\*.jpg")
# print(images)

labels_folder = r"open_pleat_final_train_and_split\val\labels"
import cv2
for image in images:
    check_pleat(image)
    image_read = cv2.imread(image,1)
    h,w,_ = image_read.shape

    image_name = image.split("\\")[-1] # Get image name

    image_name = image_name[:image_name.find(".jpg")] # Remove .jpg
    print(image_name)
    with open(os.path.join(labels_folder, image_name + ".txt")) as f: # Checking the labels txt files
        read_lines = f.readlines() # read all lines of labels
        # print(read_lines)

        # line = read_lines.split("\n")
        # print(line)
        for line in read_lines: # Read each line
            line = line.replace("\n", "") # Remove \n at the endd of the labels

            clss , x1, y1, x2, y2 = line.split(" ") # Split by space 
            # print(clss , x1, y1, x2, y2 )
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

            cv2.rectangle(image_read, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image_read, clas, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("image", image_read)
        cv2.waitKey(0)
            

        break
        
        
