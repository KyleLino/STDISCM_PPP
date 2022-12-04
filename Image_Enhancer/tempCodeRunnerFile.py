 #gets extension of the current image file
        partitioned_string = re.split(',|_|/', image_file)
        #for naming convention
        extension_string = image_file.partition('.')