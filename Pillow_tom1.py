from PIL import Image

image1 = Image.open("Adriana\\Adriana12.jpg")

print(image1.size)
print(image1.format)

# It will open with the default program that is there to open the images.
image1.show()

# For cropping the image we will use crop function over image object.
area = (0,0,400,300)
image1_cropped = image1.crop(area)

print("")
print("Image after being cropped")
    
image1_cropped.show()
print(image1_cropped.size)
print(image1_cropped.format)