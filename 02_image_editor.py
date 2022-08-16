"""This script allows for conversion of image files to png or jpg and also allows for resizing images
    while maintaining aspect ratios"""
import os
from os import path

from PIL import Image

image_dir = r"C:\Users\ryanl\Desktop\Programming\Images"


def convert_to_png(img_directory):
    # path for new folder to be created
    png_dir = os.path.join(img_directory, 'png_imgs')
    # create new folder if not already created
    if not path.exists(png_dir):
        try:
            os.mkdir(png_dir)
        except OSError as err:
            print("OS error: {0}".format(err))
    else:
        print("folder already created")
    # Loop through directory where images are stored
    for f in os.listdir(img_directory):
        # only open image files
        if f.endswith((".jpeg", ".jpg", ".jfif", ".gif")):
            # Add the file name to end of directory and open image
            im = Image.open(os.path.join(img_directory, f))
            # Split the file name (fn) and file extension (fext)
            fn, fext = os.path.splitext(f)
            # Save the images in new folder as png's
            im.save((os.path.join(png_dir, fn + ".png")))


def convert_to_jpg(img_directory):
    # path for new folder to be created
    jpg_dir = os.path.join(img_directory, 'jpg_imgs')

    # create new folder if not already created
    if not path.exists(jpg_dir):
        try:
            os.mkdir(jpg_dir)
        except OSError as err:
            print("OS error: {0}".format(err))
    else:
        print("folder already created")

    # Loop through directory where images are stored
    for f in os.listdir(img_directory):
        # only open image files
        if f.endswith((".png", ".jpeg", ".jfif", ".gif")):
            # Add the file name to end of directory and open image
            im = Image.open(os.path.join(img_directory, f))
            # Split the file name (fn) and file extension (fext)
            fn, fext = os.path.splitext(f)
            # Save the images in new folder as jpg's
            im.save((os.path.join(jpg_dir, fn + ".jpg")))


def resize_img(img_directory):
    w = int(input("Enter width of img: "))
    h = int(input("Enter height of img: "))
    size = (w, h)
    # path for new folder which will be named as the dimensions of the image
    resize_dir = os.path.join(img_directory, '{}_{}'.format(w, h))
    # create new folder if not already created
    if not path.exists(resize_dir):
        try:
            os.mkdir(resize_dir)
        except OSError as err:
            print("OS error: {0}".format(err))
    else:
        print("folder already created")
    # Loop through directory where images are stored
    for f in os.listdir(img_directory):
        # only open image files
        if f.endswith((".png", ".jpeg", ".jpg", ".jfif", ".gif")):
            im = Image.open(os.path.join(img_directory, f))
            # thumnail maintains aspect ratio
            im.thumbnail((size))
            # save re-sized images in the newly created folder
            im.save(os.path.join(resize_dir, f))


usr_in = input("To convert images to jpg type jpg \nTo convert images to png type png "
               "\nTo resize images type resize \n")
if usr_in == "jpg":
    convert_to_jpg(image_dir)
elif usr_in == "png":
    convert_to_png(image_dir)
elif usr_in == "resize":
    resize_img(image_dir)
else:
    print("Invalid entry, try again")
