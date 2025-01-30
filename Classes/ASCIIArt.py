from PIL import Image
import numpy
import tkinter as tk
from rembg import remove


ASCIIGradient = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.     '''
gradientLength = len(ASCIIGradient)
class ASCIIRenderer:
    # defines the ASCIIRenderer Object
    # @param img - the image, as a PIL Image object
    # @param width - the desired amount of letters across the screen to render the image
    # @param removeBackground - if true it removes the image background
    # @param hScaleFactor - Determines the stretch of the height, this is used to counteract the fact characters are taller than they are wide.
    # @return none
    def __init__(self, img,width :int,removeBackground:bool, hScaleFactor:float):
        self.hScaleFactor = hScaleFactor
        self.width = width
        self.removeBackground = removeBackground
        self.img = img
        wFactor = width/float(self.img.size[0])
        self.height = int(float(self.img.size[1])*wFactor*hScaleFactor)
        self.img = self.img.resize((width,self.height),Image.Resampling.LANCZOS)
        if(removeBackground):
            self.img = remove(self.img)
    # Takes in a value and returns a character of coresponding lightness.
    # @param val - value between 0 and 1, higher returns a lighter character.
    # @return chr, ranging from lightest to darkest
    def charFromVal(self, val:float) -> chr:
        return ASCIIGradient[int(val*gradientLength)-1]
    # Takes a rgb pixel value and returns it as a gray-scale value between 0 and 1.
    # Uses NTSC method divided by 255
    # @param tup - a tuple object of RGB
    # @return grayscale value between 0 - 1
    def rgbToGrayScale(self, tup:tuple) -> float:
        return (0.00117254901*tup[0]+0.00230196078*tup[1]+0.00044705882*tup[2])
    # Converts localized PIL image to chr array,
    # @return array of ASCII letters
    def imageToASCII(self) -> list:
        arr = numpy.array(self.img)
        return [[self.charFromVal(self.rgbToGrayScale(arr[py][px])) for px in range(0,self.width)]for py in range(0,self.height)]
    # Turns ASCII array into a printable statement
    # @return printable string
    def __str__(self) -> str:
        arr = self.imageToASCII()
        out =''
        for py in range(0,self.height):
            out+='\n'
            for px in range(0,self.width):
                out += arr[py][px]
        return out
    # Writes ASCII text to file
    # @param filePath - A string describing filePath
    # @return none
    def writeToFile(self, filePath:str) -> None:
        out = open(filePath, 'w')
        out.write(str(self))
        out.close()
    # Updates the window with image from image supplier
    # Parameters set in displayToVideo
    # @return none
    def updateWindow(self):
        self.__init__(self.imageSupplier(), self.width , self.removeBackground,self.hScaleFactor)
        self.l.config(text=str(self))
        self.l.pack()
        self.root.after(1000//self.FPS,self.updateWindow)
    #Updates the font size and width of image when slider updates.
    #Slider code inspired by https://www.geeksforgeeks.org/python-tkinter-scale-widget/
    # @param length - takes in slider value.
    # @return none
    def sliderChanged(self,length):
        self.width = int(length)
        self.l.config(font =("Courier", 2000//self.width))
    #Creates a window that updates from an image supplier. 
    # inspired by https://www.geeksforgeeks.org/python-tkinter-text-widget/ for tkinter widget
    # @param image_supplier - lambda function that supplies a PIL Image
    # @param FPS - frames per second (It may be slower becuase limits on processing speed)
    # @param width - the width of the window
    # @param height - height of the window
    # @return none
    def displayVidToWindow(self,image_supplier,FPS:int,width:int, height:int):
        self.FPS = FPS
        self.root = tk.Tk()
        self.root.geometry(str(width)+"x" + str(height))
        self.w = tk.Scale(self.root, from_= 50, to= 750, length=650,tickinterval=50, orient=tk.HORIZONTAL, command= self.sliderChanged)
        self.w.set(self.width)
        self.l =  tk.Label(self.root, text = str(self))
        self.l.config(font =("Courier", 2000//self.width))
        self.l.pack()
        self.w.pack()
        b1 = tk.Button(self.root, text = "Exit",
                    command = self.root.destroy) 
        b1.pack()
        self.imageSupplier = image_supplier
        self.root.after(0,self.updateWindow)
        self.root.mainloop()
    #Creates a window showing ASCII image
    # inspired by https://www.geeksforgeeks.org/python-tkinter-text-widget/ for tkinter widget
    # @param width - the width of the window
    # @param height - height of the window
    # @return none
    def displayPicToWindow(self,width:int,height:int):
        root = tk.Tk()
        root.geometry(str(width)+"x" + str(height))
        l = tk.Label(root, text = str(self))
        l.config(font =("Courier", 1000//self.width))
        b1 = tk.Button(root, text = "Exit",
                    command = root.destroy) 
        
        l.pack()
        b1.pack()
        # Insert The Fact.
        
        root.mainloop()
