import os
import glob

images_path = glob.glob("train/*.jpg")

for img in images_path:
    print(os.path.split(img)[-1])
    
