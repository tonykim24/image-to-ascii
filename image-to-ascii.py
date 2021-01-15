"""
TODO:
    -hashmap and pixelsize.
    -pass in pixelsize and image path as command line argument (argparse).
"""
import sys
import os
import cv2
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="image path")
parser.add_argument("pixelsize", type=int, help="pixelating size")
args = parser.parse_args()

# https://docs.python.org/3/library/argparse.html


def divider(a):
    if (a % 10 != 0):
        return 10 - (a % 10)
    return 0


def image_to_ascii(path, pixelsize):
    # picture image
    picture = cv2.imread(path,0)
    # cv2.imshow(picture)
    # dimensions = picture.shape

    yvalue = picture.shape[0]
    xvalue = picture.shape[1]
    ypadding = divider(yvalue)
    xpadding = divider(xvalue)
    # Get picture size
    height, width = picture.shape[:2]

    pixelsize = int(pixelsize)

    # Desired "pixelated" size
    w, h = (((yvalue + ypadding) // pixelsize), ((xvalue + xpadding) // pixelsize))

    # Resize picture to "pixelated" size
    temp = cv2.resize(picture, (w, h), interpolation=cv2.INTER_LINEAR)

    # Initialize output image
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    arr = [10, 31, 52, 73, 94, 115, 136, 157, 178, 199, 220, 243, 255, 255]
    for i in range(yvalue):
        for j in range(xvalue):  
            output[i,j] = arr[output[i,j]  // 19]


    strs = ["" for x in range((yvalue + ypadding) // pixelsize)]

    dict = {10 :'@@', 31 :'$$', 52 :'##', 73 :'**', 94 :'!!', 115 :'==',
            136 :';;', 157 :'::', 178 :'~~', 199 :'--', 220 :',,', 243 :'..',
            255 :'  '}
    # hashmap and dictionary
    for i in range(0, yvalue, pixelsize):
        for j in range(0, xvalue, pixelsize):
            strs[i// pixelsize] += dict[output[i, j]]

    for line in strs:
        print (line)
    # cv2.imshow("cropped", picture)

    cv2.imshow('Output', output)
    image = cv2.copyMakeBorder(picture, 0, ypadding, 0, xpadding, cv2.BORDER_CONSTANT, None, 255)
    cv2.imshow('border', image)

    print (strs)
    print (yvalue + divider(yvalue))
    print (xvalue + divider(xvalue))

    cv2.waitKey(0)

if __name__ == "__main__":
    print(args.path)
    print(args.pixelsize)
    image_to_ascii(args.path, args.pixelsize)