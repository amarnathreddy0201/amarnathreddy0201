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
