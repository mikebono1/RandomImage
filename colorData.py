import random

class randomImage:
    #define name, size, and base color of image
    def __init__(self, name=None, height=None, width=None, r=None, g=None, b=None):
        random.seed()
        if name is not None:
            self.fileName = name
            self.filePath = self.appendFilePath(name)
        if name is None:
            self.fileName = self.createName()
            self.filePath = self.appendFilePath(self.fileName)
        if height is not None:
            if width is not None:
                self.height = height
                self.width = width
            else:
                self.height = height
                self.width = round(height * (random.randint(5, 20) / 10))
        if height is None:
            self.height = random.randint(50, 1000)
            self.width = round(self.height * (random.randint(5, 20) / 10))
        if r is None:
            self.color = self.createBaseColor()
        if r is not None:
            self.color = [r, g, b]

    #configure folder to save images
    def appendFilePath(self, name):
        return 'randomImage/images/' + name + '.png'

    #create name for file by using one adjective and noun from dictionary
    def createName(self):
        file = open('randomImage/adj.txt', 'r')
        adjLine = random.randint(0, 907)
        a = 0
        while a < adjLine:
            adjective = file.readline().rstrip('\n')
            a += 1
        file.close()
        file = open('randomImage/noun.txt', 'r')
        nounLine = random.randint(0, 6801)
        b = 0
        while b < nounLine:
            noun = file.readline().rstrip('\n')
            b += 1
        file.close()
        return adjective + noun.capitalize()

    #generate base color of palette
    def createBaseColor(self):
        c = 0
        baseColor = []
        while c < 3:
            baseColor.append(random.randint(0, 255))
            c += 1
        return baseColor

    #generates completely random RGB values
    def randomColors(self):
        c = 0;
        colorData = []
        while c < 3:
            colorData.append(random.randint(0, 255))
            c += 1
        return colorData

    #generates slow color variation pixel by pixel in a line
    def createColorPalette(self, change):
        z = 0;
        pixelData = []
        
        #generate RGB values for each pixel
        while z < 3:
            #create random difference between base and new color and operation to do
            if change is True:
                diff = random.randint(0, 5)
            else:
                diff = random.randint(0, 50)
            operation = random.randint(0, 2)

            #if operation is do nothing
            if operation == 2:
                newColor = self.color[z]

            #if operation is addition
            if operation == 1:
                #define what color this new difference makes
                if (self.color[z] + diff) > 255:
                    newColor = self.color[z] - diff
                else:
                    newColor = self.color[z] + diff
            
            #if operation is subtraction
            if operation == 0:
                #define what color this new difference makes
                if (self.color[z] - diff) < 0:
                    newColor = self.color[z] + diff
                else:
                    newColor = self.color[z] - diff

            #append new color to list
            pixelData.append(newColor)
            if change is True:
                self.color[z] = newColor
            z += 1

        return pixelData

    #create RGB data for each pixel in entire image area
    def generateColorData(self):
        data = []
        x = 0
        #generate all color data for image
        while x < self.height:
            y = 0
            rowData = []
            #generate pixel data for each row in image
            while y < self.width:
                # rowData.extend(self.createColorPalette(False))
                # rowData.extend(self.createColorPalette(True))
                rowData.extend(self.randomColors())
                y += 1
            data.append(rowData)
            x += 1
        return data

    def generateBackground(self):
        data = []
        pixelHeight = pixelWidth = 8
        x = 0
        #generate all color data for image
        while x < self.height:
            y = 0
            rowData = []
            color = self.color
            #generate pixel data for each row in image
            while y < self.width:
                c = 0
                tempColor = self.backgroundPixel(color)

                #duplicate pixel to fill effective pixel width
                while c < pixelWidth:
                    rowData.extend(tempColor)
                    c += 1
                color = tempColor
                y += 1
            
            #duplicate row pixel data to fill effective pixel height
            d = 0
            while d < pixelHeight:
                data.append(rowData)
                d += 1
            x += 1

        return data

    #create useable background for wide monitor, where each "pixel" of color is actually many pixels
    def backgroundPixel(self, color):
        x = z = 0;
        pixelData = []
        colorsToAlter = random.randint(0, 3)
        
        #generate RGB values for each pixel
        while z < 3:
            #create random difference between base and new color and operation to do
            diff = random.randint(0, 3)
            operation = random.randint(0, 7)

            #if operation is addition
            if operation > 2:
                #define what color this new difference makes
                if (color[z] + diff) > 255:
                    newColor = color[z] - diff
                else:
                    newColor = color[z] + diff
            
            #if operation is subtraction
            if operation < 2:
                #define what color this new difference makes
                if (color[z] - diff) < 0:
                    newColor = color[z] + diff
                else:
                    newColor = color[z] - diff
            
            #if operation is do nothing
            else:
                newColor = color[z]

            #append new color to list
            pixelData.append(newColor)
            z += 1
        
        # if colorsToAlter == 0:
        #     for x in range(0, 3):
        #         pixelData.append(color[x])
        # else:
        #     while 3 - colorsToAlter >= z:
        #         pixelData.append(color[z])
        #         z += 1

        return pixelData