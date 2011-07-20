import os
import unittest
from os.path import abspath
import Image

def test_jpg():
    image_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(image_path, "test.jpg")
    trial_image = Image.open(image_path)
    try:
        trial_image.load()
    except:
        print "!!!NO JPEG SUPPORT!!!"
    else:
     print "JPEG SUPPORT AVAILABLE"
if __name__ == "__main__":
    test_jpg()