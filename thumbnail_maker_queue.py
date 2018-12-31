# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.error import HTTPError
from urllib.request import urlretrieve
import threading
import PIL
from PIL import Image
from queue import Queue


FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.dl_lock = threading.Lock()
        self.download_bytes = 0;
        self.max_concurrent_dl = 4
        self.dl_sem = threading.Semaphore(self.max_concurrent_dl)
        self.images_queue = Queue()

    def download_image(self, url):
        self.dl_sem.acquire()
        # or use the with statement 
        # with self.dl_sem:
        try:
            img_filename = urlparse(url).path.split('/')[-1]
            dest_path = self.input_dir + os.path.sep + img_filename
            if not os.path.exists(dest_path):
                urlretrieve(url, dest_path)
                image_size = os.path.getsize(dest_path)
                logging.info("downloading image at URL " + url)
                logging.info(f"image [{image_size}] saved to  {dest_path}" )
            else:
                image_size = os.path.getsize(dest_path)
                logging.info(f"image [{dest_path}] exists" )

            self.images_queue.put(dest_path)
            with self.dl_lock:
                self.download_bytes += image_size

            # logging.info(f"image [{image_size}] saved to  {dest_path}" )
        finally:
            self.dl_sem.release()

    def download_images(self, img_url_list):
        # validate inputs
        if not img_url_list:
            return
        if not os.path.exists(self.input_dir):
            logging.info(f"making image dir {self.input_dir}")
            os.makedirs(self.input_dir, exist_ok=True)
        else:
            logging.info(f"image dir {self.input_dir} exists")

        logging.info("beginning image downloads")
        thread_pool = []
        start = time.perf_counter()
        for url in img_url_list:
            # download each image and save to the input dir
            t = threading.Thread(target=self.download_image, args=(url, ))
            t.start()
            thread_pool.append(t)
        for t in thread_pool:
            t.join()
        
        self.images_queue.put('poison')



        end = time.perf_counter()

        logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self):
        # validate inputs
        if not os.listdir(self.input_dir):
            return
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        while True:
            filename = self.images_queue.get()
            if not filename == 'poison':
                orig_img = Image.open(filename)
                for basewidth in target_sizes:
                    img = orig_img
                    base_name = os.path.basename(filename)
                    new_filename = os.path.splitext(base_name)[0] + \
                        '_' + str(basewidth) + os.path.splitext(base_name)[1]
                    dest_thumbnail_path = self.output_dir + os.path.sep + new_filename
                    if not os.path.exists(dest_thumbnail_path):
                        # calculate target height of the resized image to maintain the aspect ratio
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        # perform resizing
                        img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                        # save the resized image to the output dir with a modified file name
                        logging.info(f"save thumbnail image {new_filename}")
                        img.save(dest_thumbnail_path)
                    else:
                        logging.info(f"thumbnail image {dest_thumbnail_path} exists!")


                 # os.remove(self.input_dir + os.path.sep + filename)
            else:
                logging.info("poison!")
                break

        self.images_queue.task_done()


        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        self.download_images(img_url_list)
        self.perform_resizing()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
