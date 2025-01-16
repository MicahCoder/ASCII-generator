from ASCIIArt import ASCIIRenderer
from PIL import Image
img = Image.open("inputs/ladyliberty.png")
renderOb = ASCIIRenderer(img, 100, False, 1/1.41)
print(renderOb)