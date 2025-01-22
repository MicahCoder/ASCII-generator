from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
#Much inspired by @link https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
import cv2

cam = cv2.VideoCapture(0)
result,image = cam.read()
img = Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGBA))
renderOb = ASCIIRenderer(img, 400, False, .55)
renderOb.displayVidToWindow(700,700)

