from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
#Much inspired by @link https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
import cv2
def initCamera():
    try:
        return cv2.VideoCapture(0)
    except:
        return cv2.VideoCapture(1)
cam = initCamera()
def img_supplier():
    return Image.fromarray(cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGBA))
renderOb = ASCIIRenderer(img_supplier(),50,False, .55)
# renderOb.displayPicToWindow(700,700)AZ
renderOb.displayVidToWindow(img_supplier,60,1400,900)

