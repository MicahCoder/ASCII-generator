from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
import requests
from io import BytesIO
response = requests.get(input("url: "))
img =  Image.open(BytesIO(response.content))
renderOb = ASCIIRenderer(img, 600, False,.55)
renderOb.writeToFile("Outputs/jackson.txt")