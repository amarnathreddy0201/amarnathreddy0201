import logging

import cv2
from ultralytics import YOLO
import easyocr

logger = logging.getLogger(__name__)


# Initialize the OCR reader
reader = easyocr.Reader(["en"], gpu=False)


def number_plate_recognization(frame, license_plate_detector):
    try:

        # frame = cv2.resize(frame, (640, 640))

        # detect license plates
        license_plates = license_plate_detector(frame)[0]
        # print(license_plates)
        number = ""
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate

            # crop license plate
            license_plate_crop = frame[int(y1) : int(y2), int(x1) : int(x2), :]

            # process license plate
            license_plate_crop_gray = cv2.cvtColor(
                license_plate_crop, cv2.COLOR_BGR2GRAY
            )

            _, license_plate_crop_thresh = cv2.threshold(
                license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV
            )

            detections = reader.readtext(license_plate_crop_thresh)

            for detection in detections:
                bbox, text, score = detection
                number = number + "" + "".join(e for e in text if e.isalnum())

        return "".join(letter for letter in number if letter.isalnum())
    except Exception as error:
        logger.error(error)
