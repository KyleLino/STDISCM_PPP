from PIL import Image, ImageEnhance
import time
import glob
import re
import multiprocessing
import sys

#enhance functions
def main():
    #creates 900 image files from the 3 original images files 
    #images = images * 300

    #INPUTS
    #use this
    #"Image_Enhancer/input_images/*"
    image_loc = str(input('Enter image location:'))
    #use this
    #"Image_Enhancer/output_images"
    enhanced_image_loc = str(input('Enter enhanced image location:'))
    #print(images)

    #all image directories
    image_files = glob.glob(image_loc)
    #image_files = glob.glob("Image_Enhancer/input_images/*")
    #image_files = image_files * 100

    queue=multiprocessing.Queue()
    c_threads_list=[]
    COUNT = len(image_files)
    print("COUNT of images" + str(COUNT))

    time_limit = 15.0

    #print(str(images))

    for image_file in image_files:
        queue.put(image_file)

    b_in = float(input('Enter brightness value:'))
    s_in = float(input('Enter sharpness value:'))
    c_in = float(input('Enter contrast value:'))
    time_in = int(input('enter time in mins:'))
    enhancer_threads = int(input('enter no. of threads:'))

    time_in = time_in * 60
    time_limit = time_in
    
    #TXT FILE
    file_clear = open("Image_Enhancer/image_data.txt",'w')
    file_object = open('Image_Enhancer/image_data.txt', 'a')

    #LOOPS UNTIL TIME IS UP
    start_time = time.time()
    while time.time() - start_time < time_limit and queue.empty() == False:
        #LOOPS UNTILE ALL FILES ARE ENHANCED
        for n in range(enhancer_threads):
            c=consumer(COUNT, n, queue,b_in,s_in,c_in,enhancer_threads,start_time,time_limit, enhanced_image_loc)
            c_threads_list.append(c)
            c.start()
            if time.time() - start_time >= time_limit:
                break
        
        for c in c_threads_list:
            c.join()
        
    
    print('done')
    file_object_read = open('Image_Enhancer/image_data.txt', 'r')
    counter = len(file_object_read.readlines())

    #TEXT FILE
    file_object = open('Image_Enhancer/image_data.txt', 'a')
    file_object.write('\nIMAGES ENHANCED:'+ str(counter)+ '\n')
    file_object.close()
    exit()

def enhance(image_file, id,b,s,c,e_image_loc):
        
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
                new_frame = brightness_enhancer.enhance(float(b))
                sharpness_enhancer = ImageEnhance.Sharpness(new_frame)
                new_frame = sharpness_enhancer.enhance(float(s))
                contrast_enhancer = ImageEnhance.Contrast(new_frame)
                new_frame = contrast_enhancer.enhance(float(c)) 
                new.append(new_frame)

            #save part
            new[0].save(str(e_image_loc)+'/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1]), append_images=new[1:], save_all=True, loop = 0, duration = 1)
            file_object.write(str(e_image_loc)+'/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1] + '\n'))
    
    #PNG/JPG/JPEG
        else:
            #enhance part
            brightness_enhancer = ImageEnhance.Brightness(image)
            image = brightness_enhancer.enhance(float(b))
            sharpness_enhancer = ImageEnhance.Sharpness(image)
            image = sharpness_enhancer.enhance(float(s))
            contrast_enhancer = ImageEnhance.Contrast(image)
            image = contrast_enhancer.enhance(float(c)) 
            #save part
            image.save(str(e_image_loc)+'/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1]))
            file_object.write(str(e_image_loc)+'/enhanced_'+ str(id)+ '_' + str(partitioned_string[len(partitioned_string) - 1] + '\n'))

class consumer (multiprocessing.Process):
    def __init__(self, count, thread_ID, queue,b,s,c,n_threads, s_time, t_limit, e_image_loc):
        multiprocessing.Process.__init__(self)
        self.counter=int((count/n_threads))
        self.image_file=0
        self.ID=thread_ID
        self.queue=queue
        self.b = b
        self.s = s
        self.c = c
        self.start_time = s_time
        self.time_limit = t_limit
        self.enhanced_image_loc = e_image_loc
    def run(self):
        print("Consumer %i is waiting \n"%(self.ID))
        for i in range(self.counter):
            if self.queue.empty():
                break
            self.image_file=self.queue.get()
            print(self.image_file)
            enhance(self.image_file, self.ID,self.b,self.s,self.c, self.enhanced_image_loc)
            if time.time() - self.start_time >= self.time_limit:
                break
        

if __name__=="__main__":
    main()
    