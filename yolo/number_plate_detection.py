import cv2
from ultralytics import YOLO

import easyocr
import string

# Initialize the OCR reader
reader = easyocr.Reader(["en"], gpu=False)


# Mapping dictionaries for character conversion
dict_char_to_int = {"O": "0", "I": "1", "J": "3", "A": "4", "G": "6", "S": "5"}

dict_int_to_char = {"0": "O", "1": "I", "3": "J", "4": "A", "6": "G", "5": "S"}


def license_complies_format(text):
    """
    Check if the license plate text complies with the required format.

    Args:
        text (str): License plate text.

    Returns:
        bool: True if the license plate complies with the format, False otherwise.
    """
    if len(text) != 10:
        return False

    if (
        (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys())
        and (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys())
        and (
            text[2] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or text[2] in dict_char_to_int.keys()
        )
        and (
            text[3] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or text[3] in dict_char_to_int.keys()
        )
        and (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys())
        and (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys())
        and (
            text[2] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or text[2] in dict_char_to_int.keys()
        )
        and (
            text[3] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or text[3] in dict_char_to_int.keys()
        )
        and (
            text[2] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or text[2] in dict_char_to_int.keys()
        )
        and (
            text[3] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or text[3] in dict_char_to_int.keys()
        )
    ):
        return True
    else:
        return False


def read_license_plate(license_plate_crop):
    """
    Read the license plate text from the given cropped image.

    Args:
        license_plate_crop (PIL.Image.Image): Cropped image containing the license plate.

    Returns:
        tuple: Tuple containing the formatted license plate text and its confidence score.
    """

    detections = reader.readtext(license_plate_crop)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(" ", "")
        print(text)

        if license_complies_format(text):
            return format_license(text), score

    return None, None


def format_license(text):
    """
    Format the license plate text by converting characters using the mapping dictionaries.

    Args:
        text (str): License plate text.

    Returns:
        str: Formatted license plate text.
    """
    license_plate_ = ""
    mapping = {
        0: dict_int_to_char,
        1: dict_int_to_char,
        4: dict_int_to_char,
        5: dict_int_to_char,
        6: dict_int_to_char,
        2: dict_char_to_int,
        3: dict_char_to_int,
    }
    for j in [0, 1, 2, 3, 4, 5, 6]:
        if text[j] in mapping[j].keys():
            license_plate_ += mapping[j][text[j]]
        else:
            license_plate_ += text[j]

    return license_plate_


def main(frame):
    # frame = cv2.imread(
    #     r"C:\Users\alluv\Downloads\new_dataset_for truck\morning\telescopic\snapshot1_245.jpg",
    #     1,
    # )

    frame = cv2.resize(frame, (640, 640))
    license_plate_detector = YOLO("number_plate_detection1.pt")

    # detect license plates
    license_plates = license_plate_detector(frame)[0]
    print(license_plates)
    number = ""
    for license_plate in license_plates.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = license_plate

        # crop license plate
        license_plate_crop = frame[int(y1) : int(y2), int(x1) : int(x2), :]

        # process license plate
        license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)

        # cv2.imshow("license plate", license_plate_crop)
        # cv2.waitKey(0)

        _, license_plate_crop_thresh = cv2.threshold(
            license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV
        )

        detections = reader.readtext(license_plate_crop_thresh)
        print("detections : ", detections)

        for detection in detections:
            bbox, text, score = detection
            number = number + "" + "".join(e for e in text if e.isalnum())

        print("number : ", number)

    return "".join(letter for letter in number if letter.isalnum())

    # cv2.imshow("license_plate_crop_thresh plate", license_plate_crop_thresh)
    # cv2.waitKey(0)

    # # read license plate number
    # license_plate_text, license_plate_text_score = read_license_plate(
    #     license_plate_crop_thresh
    # )

    # print(license_plate_text)


# main()


def video_stream():
    video_path = r"C:\Development\aivision-pi\Tippers Formation of Line for Loading of Sand _ Lorry Videos _ Truck Videos _ TIPPER LORRY TRUCK (3) - Trim.mp4"

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        window_name = "Image"

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX

        # org
        org = (50, 50)

        # fontScale
        fontScale = 1

        # Blue color in BGR
        color = (255, 0, 0)

        # Line thickness of 2 px
        thickness = 2
        number = main(frame)

        print("@@@@@@@@@@@@@@@@@@@@@@@ number : ", type(number), number)
        # Using cv2.putText() method

        if number is None or number == "":
            print("@@@@@@@@@@@@@@@@@@@@@@@ number : ", number)
            continue
        frame = cv2.putText(
            frame,
            "number" + number,
            org,
            font,
            fontScale,
            color,
            thickness,
            cv2.LINE_AA,
        )

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


# video_stream()

frame = cv2.imread(r"C:\Development\aivision-pi\image_210.jpg", 1)

plate = main(frame)

if plate == None or plate == "":
    print("plate : ", plate)
    plate = "000000"
print("plate : ", plate)
# print(main(frame))
