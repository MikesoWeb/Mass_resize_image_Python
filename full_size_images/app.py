import os
import glob
import time
from PIL import Image

size = 128, 128


def decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time() - start_time
        print(f'Функция выполнила работу за {end_time} секунд')

    return wrapper


@decorator
def resize_image():
    for image in glob.glob('*.jpg'):
        file, ext = os.path.splitext(image)
        with Image.open(image) as im:
            im.thumbnail(size)
            im.save('new_img/' + file + 'thumbnail' + '.jpg', "JPG")


resize_image()
