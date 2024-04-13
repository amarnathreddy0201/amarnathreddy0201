import cv2
import os
import glob


def get_images_in_directory(directory):
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
    images = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                images.append(os.path.join(root, file))

    return images


sr = cv2.dnn_superres.DnnSuperResImpl_create()
_path = os.path.join(os.getcwd(), "models", "FSRCNN_x3.pb")
sr.readModel(_path)
sr.setModel("fsrcnn", 3)

path = r"C:\Users\alluv\Downloads\new_dataset_for truck"


images = get_images_in_directory(path)

out_put_directory = "new_dataset"
output_test = os.path.join(os.getcwd(), out_put_directory)

# output_test = os.path.join(r"E:\new_datset_augmented", out_put_directory)

os.makedirs(output_test, exist_ok=True)


print()

for im in images:
    image_name = im.split("\\")[-1]

    im = cv2.imread(im, 1)

    denosing = cv2.fastNlMeansDenoisingColored(im, None, 1, 1, 21, 21)
    upsample = sr.upsample(denosing)

    # image_name = "3x_" + image_name
    # cv2.imwrite(os.path.join(output_test, image_name), upsample)

    # hori = cv2.flip(upsample, 1)
    # image_name = "3x_hori_" + image_name
    # cv2.imwrite(os.path.join(output_test, image_name), hori)

    # vert = cv2.flip(upsample, 0)
    # image_name = "3x_vert_" + image_name
    # cv2.imwrite(os.path.join(output_test, image_name), vert)

    h_r = cv2.flip(upsample, -1)
    image_name = "3x_h_r" + image_name
    cv2.imwrite(os.path.join(output_test, image_name), h_r)

    print("##################")
