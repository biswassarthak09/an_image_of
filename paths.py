"""
Setup global paths for the project from environment variables.
"""
import os

CV_PATH_VOC = os.environ.get(
    "CV_PATH_VOC", "/project/dl2025s/lmbcvtst/public/data/VOCdevkit/VOC2012")
CV_PATH_CKPT = os.environ.get(
    "CV_PATH_CKPT", "/project/dl2025s/lmbcvtst/public/ckpt")
CV_PATH_DDPM = os.environ.get(
    "CV_PATH_DDPM", "/project/dl2025s/lmbcvtst/public/ddpm")

CV_PATH_VOC = os.environ.get(
    "CV_PATH_VOC", "/home/lmb/dllab2025s/public/data/VOCdevkit/VOC2012")
CV_PATH_CKPT = os.environ.get(
    "CV_PATH_CKPT", "/home/lmb/dllab2025s/public/ckpt")
CV_PATH_DDPM = os.environ.get(
    "CV_PATH_DDPM", "/home/lmb/dllab2025s/public/data/image_gen")

# CV_PATH_VOC = os.environ.get(
#     "CV_PATH_VOC", "../data/VOCdevkit/VOC2012")
# CV_PATH_CKPT = os.environ.get(
#     "CV_PATH_CKPT", "../ckpt")


# uncomment below for local dataset and model
# CV_PATH_VOC = "data/VOCdevkit/VOC2012"
# CV_PATH_CKPT = "ckpt"
