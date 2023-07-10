import numpy as np
import cv2 as cv
import glob
import os

calib_data_path = "../calib_data"

data = np.load(f"{calib_data_path}/MultiMatrix.npz")

camMatrix = data["camMatrix"]
distCof = data["distCoef"]
rVector = data["rVector"]
tVector = data["tVector"]
objPoints3D = data["objPoints3D"]
img_points_2D = data["imgPoints2D"]

print("loaded calibration data successfully")
print("Validation ...")

mean_error = 0
for i in range(len(objPoints3D)):
    imgpoints2, _ = cv.projectPoints(objPoints3D[i], rVector[i], tVector[i], camMatrix, distCof)
    error = cv.norm(img_points_2D[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "Total error: {}".format(mean_error/len(objPoints3D)) )
