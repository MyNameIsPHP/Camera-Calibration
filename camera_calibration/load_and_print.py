import cv2 as cv
import os
import numpy as np
calib_data_path = "../calib_data_70"

data = np.load(f"{calib_data_path}/MultiMatrix.npz")

camMatrix = data["camMatrix"]
distCof = data["distCoef"]
rVector = data["rVector"]
tVector = data["tVector"]

print("loaded calibration data successfully")

print("camMatrix:\n", camMatrix)
print("distCof:\n", distCof)
# print("rVector", rVector)
# print("tVector", tVector)