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
brightness_factor = 1.1
sharpness_factor = 2
contrast_factor = 3
#number of images saved
x = 0

#LOOPS UNTIL ALL FILES ARE ENHANCED
for image_file in images:
    image = Image.open(image_file)


    x += 1 #counter

    #gets extension of the current image file
    partitioned_string = re.split(',|_|/', image_file)
    extension_string = image_file.partition('.')
    print()
    print(str(extension_string))
    #save part

    #GIF
    if str(extension_string[len(extension_string) - 1]) == 'gif':
        new = []
    
        for frame_num in range(image.n_frames):
            image.seek(frame_num)
            new_frame = Image.new('RGB', image.size)
            new_frame.paste(image)
            new_frame = new_frame.convert(mode='RGB')

            brightness_enhancer = ImageEnhance.Brightness(new_frame)
            new_frame = brightness_enhancer.enhance(brightness_factor)
            sharpness_enhancer = ImageEnhance.Sharpness(new_frame)
            new_frame = sharpness_enhancer.enhance(sharpness_factor)
            contrast_enhancer = ImageEnhance.Contrast(new_frame)
            new_frame = contrast_enhancer.enhance(contrast_factor) 
            new.append(new_frame)

        new[0].save('Image_Enhancer/output_images/enhanced_'+ str(partitioned_string[len(partitioned_string) - 1]), append_images=new[1:], save_all=True)
    #png / jpeg / jpg
    else:

        brightness_enhancer = ImageEnhance.Brightness(image)
        image = brightness_enhancer.enhance(brightness_factor)
        sharpness_enhancer = ImageEnhance.Sharpness(image)
        image = sharpness_enhancer.enhance(sharpness_factor)
        contrast_enhancer = ImageEnhance.Contrast(image)
        image = contrast_enhancer.enhance(contrast_factor) 
        image.save('Image_Enhancer/output_images/enhanced_'+ str(partitioned_string[len(partitioned_string) - 1]))


