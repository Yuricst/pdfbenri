"""
Select subset of pages from pdf
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
from tqdm import tqdm


def select_pages(filepath, start=1, end=2, outfile='output.pdf'):
    """
    Add margin to pdf

    Args:
        filepath (str): path to the pdf file, including file name and extension (.pdf)
        side_margin (int): side-margins (left & right)
        height_margin (int): height-margins (top & bottom)
    """
    with open(filepath, 'rb') as f:
        p = PdfFileReader(f)
        info = p.getDocumentInfo()
        number_of_pages = p.getNumPages()

        writer = PdfFileWriter()
        #print(f'margin: {margin}')
        for i in tqdm(range(number_of_pages)):
            if start-1 <= i <= end-1:
                page = p.getPage(i)
                writer.addPage(page)

        with open(outfile, 'wb') as f:
            writer.write(f)


if __name__ == '__main__':
    filepath = input('.pdf file to add margin: ')
    select_pages(filepath, 1, 500)