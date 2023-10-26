import img2pdf
from PIL import Image
import os
from pathlib import Path

def convert_to_pdf(src):

    def convert(image, target=None):
        if not target:
            target = image.replace('.jpg', '.pdf')

        image_file = Image.open(image)
    
        pdf_bytes = img2pdf.convert(image_file.filename)
    
        # opening or creating pdf file
        file = open(target, "wb")
    
        # writing pdf files with chunks
        file.write(pdf_bytes)

        # closing image file
        image_file.close()

        # closing pdf file
        file.close()  
        
        # output
        print("Successfully converted to pdf file")

    if os.path.isfile(src):
        convert(src)    
        return


    target_dir = os.path.join(src, 'pdf')
    try:
        os.mkdir(target_dir)
    except FileExistsError:
        pass

    for image in list(Path(src).glob('*.jpg')):
        convert(image, os.path.join(target_dir, os.path.basename(image).replace('.jpg','.pdf')))
        

if __name__ == '__main__':
    src=""
    convert_to_pdf(src)


