from PIL import Image, ImageEnhance
import glob
import re

#number of images saved
x = 0

#enhance function
def enhance_image(image):
        brightness_enhancer = ImageEnhance.Brightness(image)
        image = brightness_enhancer.enhance(brightness_factor)
        sharpness_enhancer = ImageEnhance.Sharpness(image)
        image = sharpness_enhancer.enhance(sharpness_factor)
        contrast_enhancer = ImageEnhance.Contrast(image)
        image = contrast_enhancer.enhance(contrast_factor) 
        return image

#all image directories
images = glob.glob("Image_Enhancer/input_images/*")

#creates 900 image files from the 3 original images files 
#images = images * 300

#"Image_Enhancer/input_images/*"
#image_loc = str(input('Enter image location:'))
#"Image_Enhancer/output_images"
#enhanced_image_loc = str(input('Enter enhanced image location:'))
#b = int(input('Enter brightness value:'))
#s = int(input('Enter sharpness value:'))
#c = int(input('Enter contrast value:'))
#print(images)

#FACTORS
brightness_factor = .5
sharpness_factor = 2
contrast_factor = 3
#brightness_factor = b
#contrast_factor = c
#sharpness_factor = s

#print(str(images))

#TXT FILE
file_clear = open("Image_Enhancer/image_data.txt",'w')
file_object = open('Image_Enhancer/image_data.txt', 'a')

#LOOPS UNTIL ALL FILES ARE ENHANCED
for image_file in images:
    x += 1 #counter
    image = Image.open(image_file)
    
    #gets extension of the current image file
    partitioned_string = re.split(',|_|/', image_file)
    #for naming convention
    extension_string = image_file.partition('.')
    print()
    print(str(extension_string))
    
    #GIF
    if str(extension_string[len(extension_string) - 1]) == 'gif':
        new = []
    
        for frame_num in range(image.n_frames):
            image.seek(frame_num)
            new_frame = Image.new('RGB', image.size)
            new_frame.paste(image)
            new_frame = new_frame.convert(mode='RGB')
            #enhance part
            new_frame = enhance_image(new_frame)
            new.append(new_frame)

        #save part
        new[0].save('Image_Enhancer/output_images/enhanced_'+ str(x)+ '_' + str(partitioned_string[len(partitioned_string) - 1]), append_images=new[1:], save_all=True, loop = 0, duration = 1)
        file_object.write('Image_Enhancer/output_images/enhanced_'+ str(x)+ '_' + str(partitioned_string[len(partitioned_string) - 1] + '\n'))
    #PNG/JPG/JPEG
    else:
        #enhance part
        image = enhance_image(image)
        #save part
        image.save('Image_Enhancer/output_images/enhanced_'+ str(x)+ '_' + str(partitioned_string[len(partitioned_string) - 1]))
        file_object.write('Image_Enhancer/output_images/enhanced_'+ str(x)+ '_' + str(partitioned_string[len(partitioned_string) - 1] + '\n'))

file_object.write('\nIMAGES ENHANCED:'+ str(x)+ '\n')
file_object.close()