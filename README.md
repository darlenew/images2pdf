# images2pdf.py

Merge a set of images into a single PDF document.

So my sister gave me 48 screencaps from her iPad in PNG format.  I wanted to view them in the Kindle iPhone app, so I wrote this script to stitch all the PNGs together into a single 48-page PDF document. This should actually work with other image formats (assuming they are supported by the PIL/Pillow).

# Requirements
  * Pillow - https://pypi.python.org/pypi/Pillow/2.8.2
  * PyPDF2 - http://pythonhosted.org/PyPDF2/

# Usage
`$ images2pdf.py image_dir pdf_file`
* `image_dir` is the directory containing the images you want to add to the PDF
* `pdf_file` is the PDF path that you want to add images to

# TODO
* rescale or resize the images so that the pages in the output PDF are easier to view on the iPhone
* add an option to rotate the images
