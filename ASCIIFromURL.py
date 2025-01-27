from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
import requests
from io import BytesIO
response = requests.get(input("url: "))
img =  Image.open(BytesIO(response.content))
renderOb = ASCIIRenderer(img, 500, True,.55)
renderOb.displayPicToWindow(700,700)
# renderOb.displayToWindow(700,800)