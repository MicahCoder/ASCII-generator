from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
img = Image.open("inputs/statue.jpg")
renderOb = ASCIIRenderer(img, 400, False, .55)
renderOb.displayPicToWindow(700,800)