from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
#Much inspired by @link https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
import cv2

def img_supplier():
    cam = cv2.VideoCapture(0)
    result,image = cam.read()
    return Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGBA))
renderOb = ASCIIRenderer(img_supplier(),50,False, .55)
# renderOb.displayPicToWindow(700,700)
renderOb.displayVidToWindow(img_supplier,60,1400,900)

