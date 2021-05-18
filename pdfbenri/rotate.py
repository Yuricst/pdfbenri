"""
Function to rotate pdf file
Dependency: PyPDF2
"""

import PyPDF2


def rotate_pdf(pdffle, clockwise_angle=90):
	"""Function to rotate pdf"""
	pdf_in = open(pdffle, 'rb')
	pdf_reader = PyPDF2.PdfFileReader(pdf_in)
	pdf_writer = PyPDF2.PdfFileWriter()

	for pagenum in range(pdf_reader.numPages):
	    page = pdf_reader.getPage(pagenum)
	    if pagenum % 2:
	        page.rotateClockwise(clockwise_angle)
	    pdf_writer.addPage(page)

	pdf_out = open('rotated.pdf', 'wb')
	pdf_writer.write(pdf_out)
	pdf_out.close()
	pdf_in.close()

	print("Done!")


# if used from the command line, pass as argument the PDF file
if __name__ == "__main__": 
	# get file path to pdf file
	if len(sys.argv)==1:
	    raise Excepton("Please pass .pdf file path!")
	filepath = sys.argv[1]

	# get angle (if not passed, use default angle)
	if len(sys.argv)==3:
		clockwise_angle = sys.argv[2]
	else:
		clockwise_angle = 90

	rotate_pdf(filepath, clockwise_angle)

