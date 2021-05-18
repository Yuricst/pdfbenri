#!/usr/bin/env python3
"""
Merge pdfs and append page number
Yuri Shimane, 2020/09/30

Command line usage:

python merge_pdfs.py
python merge_pdfs.py <path where source pdfs are stored> 

reference: https://qiita.com/wrblue_mica34/items/16fe8cf3f8d12ebbbe58
"""

# generic modules
import sys
import os
import time

# for merging pdf
import glob
import PyPDF2

# for numerating pages
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj


# ----------------------------------------------------------------- #
# merge pdfs
# find source pdf directory
if len(sys.argv)==1:
	#source_dir = './source_pdfs'
    source_dir = input('Source path (grabbing all pdfs here): ')
else:
	source_dir = sys.argv[1]

print(f'Taking pdfs from {source_dir}...')

# import all pdfs in the source directory
source_path = source_dir + '/*.pdf'
pdffiles = glob.glob(source_path)
print(f'Merging {len(pdffiles)} pdf files... ')

# create merger object
merger = PyPDF2.PdfFileMerger()
# merge all objects
for f in pdffiles:
    merger.append(f)


# create directory where output pdf is taken
savepath = source_dir + '/merged_pdf/'
if not os.path.exists(savepath):
    os.makedirs(savepath)


# save version without page number
timestamp = time.strftime('%m%d_%H%M')
flename_nopagenum = 'merge_' + timestamp + '_no_page_numbers.pdf'
save_path_nopagenum = savepath + flename_nopagenum
merger.write(save_path_nopagenum)   # output merged files
merger.close()


# ----------------------------------------------------------------- #
# append page numbers to generated pdf
# if len(sys.argv) != 2 or ".pdf" not in sys.argv[1].lower():
#     print(f"Usage: python {sys.argv[0]} <pdf filename>")
#     sys.exit()
input_file = save_path_nopagenum
output_file = savepath + 'merge_' + timestamp + ".pdf"

reader = PdfReader(input_file)
pages = [pagexobj(p) for p in reader.pages]

canvas = Canvas(output_file)

for page_num, page in enumerate(pages, start=1):
    canvas.doForm(makerl(canvas, page))

    footer_text = f"{page_num}/{len(pages)}"
    canvas.saveState()
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setFont('Times-Roman', 14)
    canvas.drawString(290, 10, footer_text)
    canvas.restoreState()
    canvas.showPage()

# ----------------------------------------------------------------- #
# save output

canvas.save()

print(f'Done, saved at {output_file}!')

