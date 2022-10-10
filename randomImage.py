import png
import colorData

image = colorData.randomImage(None, 135, 480, 176, 243, 255)

#create and save image
png.from_array(image.generateBackground(), 'RGB').save(image.filePath)
print("Image with dimensions", image.height, image.width, "saved as", image.fileName)