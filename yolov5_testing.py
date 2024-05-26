import torch
import os
import cv2
import logging
from datetime import datetime

logging.basicConfig( format="%(message)s - %(asctime)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

model = torch.hub.load(r"E:\github_setup\yolov5", "custom", path=r"E:\github_setup\yolov5\runs\train\exp\weights\best.pt", source="local")  # local repo
image = r"E:\github_setup\yolov5\filter_open_pleat_v1i_yolov5pytorch\test\images\bb68_1_jpg.rf.e2b69eb7b7e78d26e40f4480376d11bb.jpg"

frame = cv2.imread(image,1)
results_for_pleat = model(frame)
defect_set_st1 = set()
count_images_for_dll = 0

class_names =["open_pleat"]

def get_file_name_forstation(count_images_for_dll,station):
    output_dir = "station2"
    if station == "st1":
        output_dir = "station1"
    os.makedirs(output_dir,exist_ok=True)
    

    present_time = datetime.now()
    formatted_time = present_time.strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{output_dir}/image{count_images_for_dll}_{formatted_time}.jpg"

    return filename

results_for_pleat = model(image)

defect_set_st1 = set()
count_images_for_dll = 0

for result in results_for_pleat.xyxy:
    for box in result:

        x1, y1, x2, y2, conf, cls = box
        print(x1, y1, x2, y2, conf, cls)
        x, y, width, height = int((x1 + x2) / 2), int((y1 + y2) / 2), int(x2 - x1), int(y2 - y1)

        print(x, y, width, height)

        # name = result.names[int(cls)]
        if 0 <= cls < len(class_names):
            name = class_names[int(cls)]
        else:
            name = 'Unknown'
        print(name)
        confidence = float(conf)

        print(confidence)
        
        logger.info(f"Confidence level of openpleat_model {confidence}")
        if name == "open_pleat":

            defect_set_st1.add("Middle pleat open")
            logger.info("open_pleat detection at station1")
            
            cv2.rectangle(frame, (x - width // 2, y - height // 2),
                          (x + width // 2, y + height // 2), (0, 0, 255), 2)
            
            cor = (x - width // 2 - 5, y - height // 2 - 5)
            fs = 1
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            text_color = (0, 255, 0)
            thickness = 1
            combined_text = f"{name} and {confidence}"
            
            cv2.putText(frame, combined_text, cor, font, fs,
                        text_color, thickness, cv2.LINE_AA)
            
            filename = get_file_name_forstation(count_images_for_dll, 'st1')
            cv2.imshow("image", frame)
            cv2.waitKey(0)
            count_images_for_dll += 1

cv2.imshow("image", frame)
cv2.waitKey(0)
