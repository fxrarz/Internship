"""
IMAGE PROCESSING

Requirement: CPU

Written on: 3 April 2022

Tested on: Linux(debian)

Author: A.S. Faraz Ahmed

Description:

    Sample input:
    ***For image names refer the respectve folder***

    Enter the threat image name? 2
    Enter the baggage image name?4
    Saved as: 5.jpg in sample_output_images
    
"""
import cv2
import numpy as np
import random

def gray(img,show=0):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if show == 1:
        cv2.imshow("GRAY",gray)
        cv2.waitKey(0)
    return gray
    
def threshold(img, show=0):
    th, threshed = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY_INV)    
    if show == 1:
        cv2.imshow("THRESHOLD",threshed)
        cv2.waitKey(0)
    return threshed

def remove_noise(img, show=0):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    if show == 1:
        cv2.imshow("THRESHOLD",morphed)
        cv2.waitKey(0)
    return morphed

def crop(img, show=0):
    cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]
    x,y,w,h = cv2.boundingRect(cnt)
    dst = original_img[y-18:y+h+25, x-18:x+w+25]
    if show == 1:
        cv2.imshow("CROPED",dst)
        cv2.waitKey(0)
    return dst

def downsize(img, show=0):
    scale_percent = 50
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    if show == 1:
        cv2.imshow("CROPED",resized)
        cv2.waitKey(0)
    return resized

def rotate(img, show=0):
    image_center = tuple(np.array(img.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, 45, 1.0)
    rotated = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    if show == 1:
        cv2.imshow("ROTATED",rotated)
        cv2.waitKey(0)
    return rotated

if __name__ == '__main__':
    print("***For image names refer the respectve folder***\n")
    threat_image = str(input("Enter the threat image name?"))
    baggage_image = str(input("Enter the baggage image name?"))

    original_img = cv2.imread("./threat_images/" + threat_image + ".jpg")
    gray_img = gray(original_img)
    threshold_img = threshold(gray_img)
    noise_img = remove_noise(threshold_img)
    crop_img = crop(noise_img)
    downsize_img = downsize(crop_img)

    crop_gray_img = gray(downsize_img)
    crop_threshold_img = threshold(crop_gray_img)
    mask_img = remove_noise(crop_threshold_img)

    bg = cv2.imread("./background_images/" + baggage_image + ".jpg")
    cv2.imshow("Baggage Image", bg)
    bg_gray= gray(bg)


    for row in range(downsize_img.shape[0]):
        for p in range(downsize_img.shape[1]):
            if mask_img[row][p] > 10:
                bg[row+bg.shape[0]//3-70][p+bg.shape[1]//3] = downsize_img[row][p]
    
    cv2.imshow("Threat Image", original_img)
    cv2.imshow("result",bg)
    cv2.waitKey(0)
    name = str(random.randint(0,22))
    cv2.imwrite("./sample_output_images/" + name + ".jpg",bg)
    print("Saved as: {}.jpg in ./sample_output_images".format(name))
