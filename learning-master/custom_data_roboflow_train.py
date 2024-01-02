# from ultralytics import YOLO
# import cv2
# import numpy as np


# def train_the_model():
#     # Load a model
#     model = YOLO("yolov8n.yaml")  # build a new model from scratch
#     # model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

#     # Use the model
#     # it will save the best.pt modulw in runs/weight/best.pt
#     model.train(
#         data=r"C:\Downloads\Hard Hat Sample.v4i.yolov8\data.yaml", # This is your yaml after creating data using roboflow
#         epochs=100,
#     )  # train the model
    
#     metrics = model.val()  # evaluate model performance on the validation set
#     results = model("halement.jpg", retina_masks=True)  # predict on an image

#     print(results[0].masks)


# def test_the_model():
    
#     model = YOLO(
#         r"C:\Users\Downloads\Hard Hat Sample.v4i.yolov8\runs\detect\train4\weights\best.pt"
#     ) # This is from above we will create best.pt and use here.
#     image = cv2.imread(
#         r"C:\Users\Downloads\Hard Hat Sample.v4i.yolov8\helment\000013_jpg.rf.bf2a8a518ea898bb6ff50718b9b5a727.jpg",
#         1,
#     )
#     results = model.predict(
#         image,
#         retina_masks=True,
#     )
#     print(results[0].masks)
#     if results[0].masks == None:
#         print("No Mask Found")
#         return  None
#     new = None
#     for result in results:
#         mask = result.masks.cpu().numpy()
#         bbox = result.boxes[0].cpu().numpy()
#         masks = mask.data.astype(bool)
#         ori_img = result.orig_img
#         for m in masks:
#             new = np.zeros_like(ori_img, dtype=np.uint8)
#             new[m] = ori_img[m]

#     cv2.imshow("image",new)
#     cv2.waitKey(0)



from ultralytics import YOLO
import cv2
import numpy as np


def train_the_model():
    # Load a model
    model = YOLO("yolov8s-seg.yaml")  # build a new model from scratch
    # model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    # it will save the best.pt modulw in runs/weight/best.pt
    model.train(
        data=r"data.yaml", # This is your yaml after creating data using roboflow
        epochs=100,
    )  # train the model
    
    metrics = model.val()  # evaluate model performance on the validation set
    results = model(r"train\images\1_jpg.rf.be6b468ff2d103d71f489d33802626ee.jpg", retina_masks=True)  # predict on an image

    print(results[0].masks)


    
def test_the_model(image,model):
    try:
        image = cv2.imread(
            image,1
        )

        cv2.imshow("image", image)
        cv2.waitKey(0)
        
        
        results = model.predict(
            image,
            retina_masks=True,
        )
        print(results[0].masks)
        if results[0].masks == None:
            print("No Mask Found")
            return  None
        new =None
        for result in results:
            mask = result.masks.cpu().numpy()
            bbox = result.boxes[0].cpu().numpy()
            masks = mask.data.astype(bool)
            ori_img = result.orig_img
            
            for m in masks:
                print(m)
                new = np.zeros_like(ori_img, dtype=np.uint8)
                new[m] = ori_img[m]
            # if new.any():
            cv2.imshow("mask", new)
            cv2.waitKey(0)
    except Exception as e:
        print(e)
import glob 
images =glob.glob(r"train\images\*.jpg")


model = YOLO(
        r"runs\segment\train\weights\best.pt"
    ) # This is from above we will create best.pt and use here.
for img in images:
    test_the_model(img,model)


