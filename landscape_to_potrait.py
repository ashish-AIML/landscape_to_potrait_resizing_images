"""
PYTHON CODE TO CONVERT LANDSCPAE IMAGES INTO POTRAIT MODE. IN LANDSCAPE IMAGES, WIDTH >> HEIGHT AND IN POTRAIT IMAGES, HEIGHT >> WIDTH.
"""

#import necessary packages
import numpy as np
import glob
from PIL import Image

#path is the directory where all the images are present. INPUT -- images with .jpg or .JPG
path = 'M:\\Datasets\\sample\\'

count=0
#def resize, since the images are resized into potrait mode resolution. 
def resize():
    images = glob.glob(path+'/*.jpg') #reads all images ending with .jpg extension
    for image in images: 
        img= image.split('.')[0]  #split the image name string with '.' and reading only its first element. Example: input = cat.jpg , output = cat
        im = Image.open(image) #reading image in Pillow format
        width, height = im.size 
        if width > height: 
            a= width 
            b= height 
            imResize = im.resize((b,a), Image.ANTIALIAS) #resize the image by swapping the widht and height respectively
            # imResize= im.rotate(90)  #this can be used if the image is in reversed orientation
            imResize.save(img + '.jpg', 'JPEG', quality=90) #saving the resized image with the same image name as the original
    count +=1 
resize() 