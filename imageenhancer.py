from PIL import Image, ImageEnhance

#read the image
im = Image.open("input_images/image_1.png")

#image brightness enhancer
enhancer = ImageEnhance.Brightness(im)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('output_images/original-image.png')

factor = 0.5 #darkens the image
im_output = enhancer.enhance(factor)
im_output.save('output_images/darkened-image.png')

factor = 1.5 #brightens the image
im_output = enhancer.enhance(factor)
im_output.save('output_images/brightened-image.png')