import os
import sys
from PIL import Image
from pathlib import Path
  
# define a function for compressing an image
def compress_image(src, verbose = False):

    def compress(file, target=None):
        if not target:
            target = file.replace('.jpg', '_c.jpg')

        picture = Image.open(file)
        print('compressing... ', file)
        picture.save(target, "JPEG", optimize = True, quality = 70)
        print('done')

    if os.path.isfile(src):
        compress(src)
        return
    
    target_dir = os.path.join(str(src), 'compressed')
    try:
        os.mkdir(target_dir)
    except FileExistsError: 
        pass

    print("compressing all .jpg files in ", src)
    for file in list(Path(src).glob('*.jpg')):
        compress(file, os.path.join(target_dir, os.path.basename(file)))

    return

def main():
    sourceDir = "D:\\Nitin\\flat_docs\\final"
    for im in os.listdir(sourceDir):

        if not os.path.isfile(im):
            print(im)
            compress_image(os.path.join(sourceDir, im))
    
if __name__ == "__main__":
    main()
