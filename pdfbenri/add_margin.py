"""
Add margin to pdf

Thanks to: 
https://gist.github.com/polonez/1fc01988935607b57f6ddcd7753acc7a
"""



from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
from tqdm import tqdm



def add_margin(filepath, side_margin=50, height_margin=40):
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
            page = p.getPage(i)
            new_page = writer.addBlankPage(
                page.mediaBox.getWidth() + 2 * side_margin,
                page.mediaBox.getHeight() + 2 * height_margin
            )
            new_page.mergeScaledTranslatedPage(page, 1, side_margin, height_margin)
            # writer.addPage(new_page)

        with open('output.pdf', 'wb') as f:
            writer.write(f)


if __name__ == '__main__':
    filepath = 'test.pdf'
    filepath = input('.pdf file to add margin: ')
    add_margin(filepath)