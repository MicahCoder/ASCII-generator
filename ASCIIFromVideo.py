from Classes.ASCIIArt import ASCIIRenderer
import cv2
import os
from PIL import Image
#Put Path to Video Here (Not stored in git becuase it's too storage intensive)
cam = cv2.VideoCapture("/Users/Period2/Downloads/VideoExample.mpg") 
def img_supplier() -> Image:
    return Image.fromarray(cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB))

renderOb = ASCIIRenderer(img_supplier(),150,False, .6)
renderOb.displayVidToWindow(img_supplier,int(cam.get(5)),1400,900)



