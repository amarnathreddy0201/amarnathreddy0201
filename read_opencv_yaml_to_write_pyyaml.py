import logging
import os
from typing import List

import cv2
import cv2 as cv
import numpy as np
import yaml

logging.basicConfig(
    filename="tube_dummy.log",
    format="Date-Time : %(asctime)s:%(levelname)s : Line No. - %(lineno)d : Messages. -%(message)s:FileName- %(filename)s",
    level=logging.INFO,
)
# Gets or creates a logger
logger = logging.getLogger(__name__)


def read_opencv_yaml_to_write_pyyaml():
    """read_opencv_yaml_to_write_pyyaml"""
    s = cv.FileStorage()
    # with open("C:/Amar/Tube_checker/calibration.yaml") as filename:

    data = s.open("C:/fwdcheckerboardandyaml/for_cpp/stereocalibration.yaml", cv.FileStorage_READ)
    print(data)
    R = s.getNode("R").mat()
    T = s.getNode("T").mat()
    CM1 = s.getNode("CM1").mat()
    CM2 = s.getNode("CM2").mat()
    dist1 = s.getNode("dist1").mat()
    dist2 = s.getNode("dist2").mat()
    height = s.getNode("height").real()
    width = s.getNode("width").real()
    rms = s.getNode("rms").real()

    data = {
        "CM1": np.asarray(CM1).tolist(),
        "dist1": np.asarray(dist1).tolist(),
        "CM2": np.asarray(CM2).tolist(),
        "dist2": np.asarray(dist2).tolist(),
        "R": np.asarray(R).tolist(),
        "T": np.asarray(T).tolist(),
        "rms": rms,
        "width": width,
        "height": height,
    }
    with open("calibration_cpp_to_python.yaml", "w") as fp:
        yaml.dump(data, fp, default_flow_style=False)
