from PIL import Image, ImageEnhance
import glob

#all image directories
images = glob.glob("Image_Enhancer/input_images/*")


#creates 900 image files from the 3 original images files 
#images = images * 300

#b = int(input('Enter brightness value:'))
#s = int(input('Enter sharpness value:'))
#c = int(input('Enter contrast value:'))

print(images)

#FACTORS
brightness_factor = 1
sharpness_factor = 1
contrast_factor = 1
#number of images saved
x = 0

for image_file in images:
    image = Image.open(image_file)

    #ENHANCERING PART
    brightness_enhancer = ImageEnhance.Brightness(image)
    image = brightness_enhancer.enhance(brightness_factor)
    sharpness_enhancer = ImageEnhance.Sharpness(image)
    image = sharpness_enhancer.enhance(sharpness_factor)
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(contrast_factor) 

    #saves enghanced images into png
    x += 1 #counter
    image.save('Image_Enhancer/output_images/enhanced_image_'+ str(x) +'.png')


