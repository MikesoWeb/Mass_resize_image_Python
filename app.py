import glob
import os
import time

from PIL import Image


def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time() - start_time
        print(f'Функция выполнила работу за {end_time} секунд')

    return wrapper


@decorator
def resize_img():
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as im:
            im.thumbnail((512, 512))
            im.save('new_img/' + file + "_thumbnail" + '.png', "PNG")


resize_img()
