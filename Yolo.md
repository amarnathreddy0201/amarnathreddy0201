### 1) Anchor box:  
```
Anchor boxes in YOLO are predefined bounding boxes with different aspect ratios and
scales used as a reference to predict an object's final bounding box.

Instead of predicting a bounding box from scratch, the model predicts offsets from these anchor boxes,
making it easier to detect objects with varying shapes and sizes.

The model assigns a ground truth object to the anchor box that has the highest Intersection over Union (IOU) with it,
allowing multiple objects to be detected within a
single grid cell.
```
         
### 2) Non max suppression:
```
Non-maximum suppression (NMS) in YOLO is a post-processing step that removes redundant,
overlapping bounding boxes for the same object, ensuring each object is detected only

once. It works by first discarding boxes with low confidence scores,
then keeping the box with the highest confidence score and removing all other boxes that have a high

overlap (Intersection over Union or IoU) with it. This process is repeated until all boxes are either selected or suppressed. 
```

### 3) Architecture
```
The architecture of YOLOv8 is divided into three main components: the backbone, neck, and head.
The backbone extracts features from the input image, the neck fuses these

features from different scales, and the head predicts bounding boxes and class probabilities.
It is built upon a convolutional neural network (CNN) and uses an advanced CSPDarknet-like structure for its backbone. 
```

### 4) Loss in Classification:
```
A loss function in classification measures how well a model's predictions match the actual class labels by quantifying the error.
Common examples include cross-entropy loss, used for probability-based classification,
and hinge loss, often used with support vector machines to maximize the margin between classes.

The goal of training is to minimize this loss function to produce more accurate predictions.
```
### 5) YOLO (You Only Look Once) Overview

         YOLO is a real-time object detection algorithm that detects objects in a single pass of a neural network.
         It divides the image into a grid and predicts bounding boxes and class probabilities simultaneously,
         making it very fast and efficient.
         
         - Key Features
         
                  - Real-time object detection
         
                  - Single-stage detection
         
                  - End-to-end training
         
                  - High speed with good accuracy
         
         - How It Works
         
                  - Image is divided into an S × S grid
         
                  - Each grid cell predicts:
         
                  - Bounding box coordinates
         
                  - Objectness score
         
                  - Class probabilities
         
                  - Non-Max Suppression removes overlapping boxes
         
         - Advantages
         
                  - Extremely fast
         
                  - Good balance of speed and accuracy
         
                  - Suitable for real-time systems
         
         - Limitations
         
                  - Struggles with very small objects
         
                  - Can have localization errors
         
         - Applications
         
                  - Self-driving cars
         
                  - Surveillance
         
                  - Drones & robotics
         
                  - Retail analytics 
