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

print("camMatrix:\n", camMatrix)
print("distCof:\n", distCof)

print("Validation ...")

mean_error = 0
for i in range(len(objPoints3D)):
    imgpoints2, _ = cv.projectPoints(objPoints3D[i], rVector[i], tVector[i], camMatrix, distCof)
    error = cv.norm(img_points_2D[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "Old total error: {}".format(mean_error/len(objPoints3D)) )


# Do manual calibration here
camMatrix[0][0] = 583.15670716
camMatrix[0][1] = 2.64481763
camMatrix[0][2] = 311.054236
camMatrix[1][1] = 581.6328274
camMatrix[1][2] = 242.00853398
print("New camMatrix:\n", camMatrix)
# [[583.15670716   2.64481763 311.054236  ]
#  [  0.         581.6328274  242.00853398]
#  [  0.           0.           1.        ]]
mean_error = 0
for i in range(len(objPoints3D)):
    imgpoints2, _ = cv.projectPoints(objPoints3D[i], rVector[i], tVector[i], camMatrix, distCof)
    error = cv.norm(img_points_2D[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "New total error: {}".format(mean_error/len(objPoints3D)) )
