from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image, ImageFilter
from cv2 import Canny
#Much inspired by @link https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
import cv2
#Camera Port can very wuith a webcam or iphone(with mac)
def initCamera():
    try:
        return cv2.VideoCapture(0)
    except:
        return cv2.VideoCapture(1)
cam = initCamera()
def img_supplier() -> Image:
    img = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
    img = Canny(image=img, threshold1 = 100, threshold2= 700)
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_GRAY2RGB))
    # img.show()
    return img
#True for background can't render quick enough
renderOb = ASCIIRenderer(img_supplier(),100,False, .55)
#renderOb.displayPicToWindow(700,700)
renderOb.displayVidToWindow(img_supplier,100,1400,900)

