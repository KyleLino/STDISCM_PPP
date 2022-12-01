from PIL import Image, ImageEnhance

#read the image
image = Image.open("Image_Enhancer/input_images/image_1.png")

#ENHANCERS
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)
contrast_enhancer = ImageEnhance.Contrast(image)

#FACTORS
brightness_factor = 1
sharpness_factor = 1
contrast_factor = 1

#ENHANCING
image_output = brightness_enhancer.enhance(brightness_factor)
image_output = sharpness_enhancer.enhance(sharpness_factor)
image_output = contrast_enhancer.enhance(contrast_factor)
image_output.save('Image_Enhancer/output_images/enhanced_image_2.png')