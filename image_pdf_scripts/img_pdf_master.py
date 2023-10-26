import compress_image
import convert_to_pdf
import merge_pdf
from pathlib import Path
import sys

def img_pdf_service(src: str):
    
    user_input = input("""choose:\n '1' to compress image \n '2' to convert image to pdf \n '3' to merge pdfs\n""")
    
    match user_input:
        case '1':
            compress_image.compress_image(src)
            return
        case '2':
            convert_to_pdf.convert_to_pdf(src)
            return
        case '3':
            merge_pdf.merge_pdfs(src)
            return
        case _:
            print(f'{user_input} is not valid input')

if __name__ == '__main__':
    
    src= sys.argv[1] if len(sys.argv)>1 else input("""Enter the source: \n""")

    img_pdf_service(src)