import cv2
import numpy as np
import time
import sys
import os
from django.conf import settings

CONFIDENCE = 0.5
SCORE_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5


def find_object_data(images):
    img_copy = images
    # the neural network configuration
    config_path = os.path.join(settings.CONFIG_MACHINE_LEARNING_ROOT, 'yolov3.cfg')
    # the YOLO net weights file
    weights_path = os.path.join(settings.CONFIG_MACHINE_LEARNING_ROOT, 'yolov3.weights')
    # loading all the class labels (objects)
    labels = open(os.path.join(settings.CONFIG_MACHINE_LEARNING_ROOT, 'coco.names')).read().strip().split("\n")
    # generating colors for each object for later plotting
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    # path_name = "images/city_scene.jpg"
    # image = cv2.imread(path_name, 0)
    # file_name = os.path.basename(path_name)
    # filename, ext = file_name.split(".")
    #
    # h, w = image.shape[:2]
    # # create 4D blob
    # blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    # print(blob)
    return img_copy
