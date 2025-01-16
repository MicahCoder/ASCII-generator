from PIL import Image
import matplotlib.pyplot as plt
import numpy
ASCIIGradient = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.     '''
gradientLength = len(ASCIIGradient)
class ASCIIRenderer:
    def __init__(self, img,width,removeBackground, hScaleFactor):
        self.width = width
        self.removeBackground = removeBackground
        if isinstance(img,str):
            self.img = Image.open(img)
        else:
            self.img = img
        wFactor = width/float(self.img.size[0])
        self.height = int(float(self.img.size[1])*wFactor*hScaleFactor)
        self.img = self.img.resize((width,self.height),Image.Resampling.LANCZOS)
    #@param val, value between 0 and 1, returns ascii constant. 
    def charFromVal(self, val):
        return ASCIIGradient[int(val*gradientLength)-1]
    #Uses NTSC method divided by 255
    def rgbToGrayScale(self, tup):
        if len(tup) == 3:
            return (0.00117254901*tup[0]+0.00230196078*tup[1]+0.00044705882*tup[2])
        else:
            return (0.00117254901*tup[0]+0.00230196078*tup[1]+0.00044705882*tup[2])*tup[3]/255
    def imageToASCII(self, img):
        arr = numpy.array(img)
        return [[self.charFromVal(self.rgbToGrayScale(arr[py][px])) for px in range(0,self.width)]for py in range(0,self.height)]
    def __str__(self):
        if(self.removeBackground):
            print("not yet")
        arr = self.imageToASCII(self.img)
        out =''
        for py in range(0,self.height):
            out+='\n'
            for px in range(0,self.width):
                out += arr[py][px]
        return out
    def writeToFile(self, filePath):
        out = open(filePath, 'w')
        out.write(str(self))
        out.close()