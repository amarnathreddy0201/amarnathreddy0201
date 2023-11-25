import yaml
import cv2 as cv
import cv2
from yaml.loader import SafeLoader
import numpy as np

if __name__ == "__main__":
   
    cv_file = cv2.FileStorage("calibration.yaml", cv2.FILE_STORAGE_WRITE)
    yam_data = {}
    with open("C:/fwdcheckerboardandyaml/for_python/stero_calibration.yaml") as f:
        data = yaml.load(f, Loader=SafeLoader)
    print(data)
   
    for key, val in data.items():
        if isinstance(val,list):
            yam_data[key] = np.asarray(val)
        else:
            yam_data[key] = val
        
        cv_file.write(key,yam_data[key])
    # # Note you *release*; you don't close() a FileStorage object
    cv_file.release()
