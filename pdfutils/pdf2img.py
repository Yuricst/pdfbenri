#!/usr/bin/env python3
"""
Converts pdf file to images
Yuri Shimane, 2021.01.01

This code requires the pdf2image module, which may be installed by

    $ conda install pdf2image

"""

import sys
import os
import shutil
from pdf2image import convert_from_path
from tqdm import tqdm


def pdf2img(filepath):
	"""Function converts pdf file to individal images of each page. 
	Images are saved in the same directory as the pdf file.

	Args:
		filepath (str): path to the pdf file, including file name and extension (.pdf)
	Returns:
		(none): generates files
	"""

	# split filepath from directory and filename
	fledir, flename = os.path.split(filepath)

	output_folder = os.path.join(fledir, "outs")
	os.mkdir( output_folder )
	images = convert_from_path( filepath , output_folder=output_folder )  # read pdf file (entire page)
	# to specify page number, pass it as argument to convert_from_path()

	# make directory to save images
	os.mkdir( os.path.join(fledir, "imagefles") )

	# save pages as images
	for i in tqdm(range(len(images))):
		save_image = "img" + str(i+1) + ".jpg"   # modify here to change file names
		images[i].save( os.path.join(fledir, "imagefles", save_image), 'JPEG')

	# remove outs directory
	shutil.rmtree(output_folder)
	print("Done!")



# if used from the command line, pass as argument the PDF file
if __name__ == "__main__": 
	# get file path to pdf file
	if len(sys.argv)==1:
	    raise Excepton("Please pass .pdf file path!")
	filepath = sys.argv[1]
	pdf2img(filepath)
