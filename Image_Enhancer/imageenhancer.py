from PIL import Image, ImageEnhance
import glob
import re

#all image directories
images = glob.glob("Image_Enhancer/input_images/*")

#creates 900 image files from the 3 original images files 
#images = images * 300

#b = int(input('Enter brightness value:'))
#s = int(input('Enter sharpness value:'))
#c = int(input('Enter contrast value:'))

#print(images)

#FACTORS
brightness_factor = .3
sharpness_factor = 1
contrast_factor = 1
#number of images saved
x = 0

#LOOPS UNTIL ALL FILES ARE ENHANCED
for image_file in images:
    image = Image.open(image_file)

    print(str(image.mode))
    image = image.convert('RGB')
    print(str(image.mode))

    #ENHANCERING PART
    brightness_enhancer = ImageEnhance.Brightness(image)
    image = brightness_enhancer.enhance(brightness_factor)
    sharpness_enhancer = ImageEnhance.Sharpness(image)
    image = sharpness_enhancer.enhance(sharpness_factor)
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(contrast_factor) 

    x += 1 #counter

    #gets extension of the current image file
    partitioned_string = re.split(',|_|/', image_file)
    extension_string = image_file.partition('.')
    print()
    print(str(extension_string))
    #save part

    if str(extension_string[len(extension_string) - 1]) == 'gif':
        image = image.convert('P')
        print('hereee')
        print()
    #png / jpeg / jpg
    else:

        brightness_enhancer = ImageEnhance.Brightness(image)
        image = brightness_enhancer.enhance(brightness_factor)
        sharpness_enhancer = ImageEnhance.Sharpness(image)
        image = sharpness_enhancer.enhance(sharpness_factor)
        contrast_enhancer = ImageEnhance.Contrast(image)
        image = contrast_enhancer.enhance(contrast_factor) 
        image.save('Image_Enhancer/output_images/enhanced_'+ str(partitioned_string[len(partitioned_string) - 1]))


