from ultralytics import YOLO
import cv2
# Load a YOLOv8 model
model = YOLO("yolov8n.pt")  # Load an official YOLOv8 nano model


def function1():
    # Perform inference
    results = model(r"c:\Users\amarn\OneDrive\Pictures\father mother.jpg")

    # Check the size of the processed input image
    processed_image_size = results.orig_shape  # Original image size (width, height)
    print(f"Original Image Size: {processed_image_size}")

    # Get the resized image dimensions used by the model
    input_image_size = results.names  # Target size used for YOLOv8 model
    print(f"Resized Image Shape (used for inference): {input_image_size}")



def function2():

    # Perform inference
    results = model(r"c:\Users\amarn\OneDrive\Pictures\father mother.jpg")

    # Access the first result in the list
    result = results[0]  # The first (and likely only) result

    # Check the original image size
    original_image_size = result.orig_shape  # Original image size (height, width)
    print(f"Original Image Size: {original_image_size}")

    # Check the resized image dimensions used by the model for inference
    resized_image_size = result.img_shape  # Resized image dimensions (height, width)
    print(f"Resized Image Shape (used for inference): {resized_image_size}")


def function3():

    # Perform inference
    results = model(r"c:\Users\amarn\OneDrive\Pictures\father mother.jpg")

    # Access the first result in the list
    result = results[0]  # The first (and likely only) result

    # Original image size
    original_image_size = result.orig_shape  # Original image size (height, width)
    print(f"Original Image Size: {original_image_size}")

    # Model's default input size (used for resizing)
    resized_image_size = model.model.args['imgsz']  # YOLO's default inference size (single value or tuple)
    print(f"Model Resized Input Shape: {resized_image_size}")



def function4():
    # Perform inference
    results = model(r"c:\Users\amarn\OneDrive\Pictures\father mother.jpg")

    # Access the first result
    result = results[0]

    # 1. Original image size (before preprocessing)
    original_image_size = result.orig_shape  # (height, width)
    print(f"Original Image Size: {original_image_size}")

    # 2. Model's input size (default or custom imgsz)
    resized_target_size = model.model.args['imgsz']  # Default input size used by YOLO (e.g., 640x640)
    print(f"Model Target Resized Shape: {resized_target_size}")

    # 3. Preprocessed image size after letterbox resizing
    resized_image_size = result.orig_img.shape[:2]  # (height, width) after resizing
    print(f"Resized Image Shape After Preprocessing: {resized_image_size}")


def function5():
    image = cv2.imread(r"c:\Users\amarn\OneDrive\Pictures\father mother.jpg",1)
    image = cv2.resize(image, (640, 640))
    # Perform inference
    results = model(image)

    # Access the first result
    result = results[0]

    # Original image shape
    orig_height, orig_width = result.orig_shape  # Original image dimensions

    # Resized image shape (after letterbox resizing)
    resized_height, resized_width = result.orig_img.shape[:2]

    # Letterbox padding
    pad_x = (resized_width - resized_height * (orig_width / orig_height)) / 2 if orig_height > orig_width else 0
    pad_y = (resized_height - resized_width * (orig_height / orig_width)) / 2 if orig_width > orig_height else 0

    # Scaling factors
    scale_x = orig_width / (resized_width - 2 * pad_x)
    scale_y = orig_height / (resized_height - 2 * pad_y)

    # Draw bounding boxes on the original image
    original_image = cv2.imread(r"c:\Users\amarn\OneDrive\Pictures\father mother.jpg")  # Load original image

    for box in result.boxes:  # Iterate through detected bounding boxes
        # Get box coordinates (x1, y1, x2, y2)
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        
        # Adjust for padding
        x1 -= pad_x
        x2 -= pad_x
        y1 -= pad_y
        y2 -= pad_y

        # Scale back to the original image size
        x1 *= scale_x
        x2 *= scale_x
        y1 *= scale_y
        y2 *= scale_y

        # Convert to integers
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

        # Draw the box on the original image
        label = result.names[int(box.cls)]  # Get the class label
        confidence = box.conf.item()  # Get the confidence score
        cv2.rectangle(original_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(original_image, f"{label}: {confidence:.2f}", ((x1), int( )), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save or display the result
    # cv2.imwrite("output.jpg", original_image)
    cv2.imshow("Result", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def function6():
    image = cv2.imread(r"d:\Downloads\MOT16\test\MOT16-01\img1\000001.jpg")

    # Perform inference
    results = model(image)
    print(results)

# function6()

def function7():
   

    # Perform inference
    results = model(r"d:\Downloads\MOT16\test\MOT16-01\img1\000001.jpg")

    # Access the first result
    result = results[0]

    # Original image shape (Height, Width)
    original_height, original_width = result.orig_shape

    # Resized image shape used for inference (Height, Width)
    resized_height, resized_width = result.orig_img.shape[:2]

    print(f"Original Image Size: {original_height}x{original_width}")
    print(f"Resized Image Shape (used for inference): {resized_height}x{resized_width}")
    # Compute scaling factors and padding
    scale_x = resized_width / original_width
    scale_y = resized_height / original_height

    # Get bounding boxes and map them back to the original image size
    for box in result.boxes:  # Iterate through each detected box
        # Get box coordinates (x1, y1, x2, y2) in the resized image
        x1, y1, x2, y2 = box.xyxy[0].tolist()

        # Scale back to original dimensions
        x1 /= scale_x
        x2 /= scale_x
        y1 /= scale_y
        y2 /= scale_y

        # Convert to integers for drawing
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

        # Get the class label and confidence
        label = result.names[int(box.cls)]  # Class label
        confidence = box.conf.item()  # Confidence score

        # Draw the bounding box and label on the original image
        original_image = cv2.imread(r"c:\Users\amarn\OneDrive\Pictures\father mother.jpg")
        cv2.rectangle(original_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(original_image, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save or display the output
    # cv2.imwrite("output_with_boxes.jpg", original_image)
    cv2.imshow("Result", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
