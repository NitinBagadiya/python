from PyPDF2 import PdfMerger
import os, sys
from pathlib import Path

def merge_pdfs(src: str):

    pdfs=list(Path(src).glob('*.pdf'))
    
    if len(pdfs)<2:
        print("Not enough files to merge!")
        sys.exit()


    # creating pdf file merger object
    merge_pdfsr = PdfMerger()
 
    # appending pdfs one by one
    for pdf in pdfs:
        merge_pdfsr.append(pdf)
 
    destination_filename = os.path.join(src, 'merged_all.pdf')
    # writing combined pdf to output pdf file
    with open(destination_filename, 'wb') as f:
        merge_pdfsr.write(f)

    print(f"successfully merged all pdfs to {destination_filename}")

if __name__ == "__main__":
    # calling the main function
    src=""
    merge_pdfs()
    