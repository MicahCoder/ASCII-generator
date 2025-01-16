from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
img = Image.open("/Users/Period2/Downloads/me.jpeg")
renderOb = ASCIIRenderer(img, 600, False, .55)
renderOb.writeToFile("Outputs/me.txt")