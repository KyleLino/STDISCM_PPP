from PIL import Image, ImageEnhance
import time
import glob
import re
import multiprocessing

#number of images saved
x = 0
#
consumer_threads = 2

#enhance functions
def main():
    #creates 900 image files from the 3 original images files 
    #images = images * 300

    #INPUTS
    #use this
    #"Image_Enhancer/input_images/*"
    #image_loc = str(input('Enter image location:'))
    #use this
    #"Image_Enhancer/output_images"
    #enhanced_image_loc = str(input('Enter enhanced image location:'))
    # 0 - inf
    #print(images)

    #all image directories
    #image_files = glob.glob(image_loc)
    image_files = glob.glob("Image_Enhancer/input_images/*")
    queue=multiprocessing.Queue()
    c_threads_list=[]
    COUNT = len(image_files)
    print("HAHAHAHAAHAHAH")
    print(COUNT)
    print("HAHAHAHAAHAHAH")

    #FACTORS
    brightness_factor = .1
    sharpness_factor = 2
    contrast_factor = 30
    #brightness_factor = b
    #contrast_factor = c
    #sharpness_factor = s
    time_limit = 5.0

    #print(str(images))

    for image_file in image_files:
        queue.put(image_file)

    print("HAHAHAHAAHAHAH")
    #print(queue.get())
    print("HAHAHAHAAHAHAH")

    #b = float(input('Enter brightness value:'))
    #s = float(input('Enter sharpness value:'))
    #c = float(input('Enter contrast value:'))

    #TXT FILE
    file_clear = open("Image_Enhancer/image_data.txt",'w')
    file_object = open('Image_Enhancer/image_data.txt', 'a')

    #LOOPS UNTIL TIME IS UP
    start_time = time.time()
    #print(time.time() - start_time)
    while time.time() - start_time < time_limit:
        #LOOPS UNTILE ALL FILES ARE ENHANCED
        for n in range(consumer_threads):
            c=consumer(COUNT, n, queue)
            c_threads_list.append(c)
            c.start()
            if time.time() - start_time >= time_limit:
                break
        
        for c in c_threads_list:
            c.join()
    
    print('done')



    #TEXT FILE
    file_object.write('\nIMAGES ENHANCED:'+ str(x)+ '\n')
    file_object.close()

def enhance(image_file, id):
        
        image = Image.open(image_file)
        file_object = open('Image_Enhancer/image_data.txt', 'a')
        
        #gets extension of the current image file
        partitioned_string = re.split(',|_|/', image_file)
        #for naming convention
        extension_string = image_file.partition('.')
        print()
        print(str(extension_string))
        
        #GIF
        if str(extension_string[len(extension_string) - 1]) == 'gif':
            new = []
        
            #enhances per frame/image of gif
            for frame_num in range(image.n_frames):
                image.seek(frame_num)
                new_frame = Image.new('RGB', image.size)
                new_frame.paste(image)
                new_frame = new_frame.convert(mode='RGB')
                #enhance part
                #new_frame = enhance_image(new_frame)
                brightness_enhancer = ImageEnhance.Brightness(new_frame)
                new_frame = brightness_enhancer.enhance(1.0)
                sharpness_enhancer = ImageEnhance.Sharpness(new_frame)
                new_frame = sharpness_enhancer.enhance(1.0)
                contrast_enhancer = ImageEnhance.Contrast(new_frame)
                new_frame = contrast_enhancer.enhance(1.0) 
                new.append(new_frame)

            #save part
            new[0].save('Image_Enhancer/output_images/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1]), append_images=new[1:], save_all=True, loop = 0, duration = 1)
            file_object.write('Image_Enhancer/output_images/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1] + '\n'))
    
    #PNG/JPG/JPEG
        else:
            #enhance part
            brightness_enhancer = ImageEnhance.Brightness(image)
            image = brightness_enhancer.enhance(1.0)
            sharpness_enhancer = ImageEnhance.Sharpness(image)
            image = sharpness_enhancer.enhance(1.0)
            contrast_enhancer = ImageEnhance.Contrast(image)
            image = contrast_enhancer.enhance(1.0) 
            #save part
            image.save('Image_Enhancer/output_images/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1]))
            file_object.write('Image_Enhancer/output_images/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1] + '\n'))

class consumer (multiprocessing.Process):
    def __init__(self, count, thread_ID, queue):
        multiprocessing.Process.__init__(self)
        self.counter=int((count/consumer_threads))
        self.image_file=0
        self.ID=thread_ID
        self.queue=queue
    def run(self):
        print("Consumer %i is waiting \n"%(self.ID))
        for i in range(self.counter):
            self.image_file=self.queue.get()
            enhance(self.image_file, self.ID)
        

if __name__=="__main__":
    main()