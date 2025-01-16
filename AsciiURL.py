from ASCIIArt import ASCIIRenderer
from PIL import Image
import requests
from io import BytesIO
response = requests.get(input("url: "))
img =  Image.open(BytesIO(response.content))
renderOb = ASCIIRenderer(img, 300, False,.55)
out = open("Outputs/output.txt", 'w')
out.write(str(renderOb))
out.close()