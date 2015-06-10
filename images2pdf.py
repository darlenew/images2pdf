#!/usr/bin/env python
"""Stitch a bunch of images into a single PDF"""
import os, shutil, sys, tempfile
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader

def images2pdf(input_dir, output_dir=None):
    """Convert all of the images in the directory to PDF files.    
    Assumes all of the files in the input_dir are images to be
    converted.
    """
    # convert in the same dir, if no output dir is specified
    output_dir = output_dir if output_dir else input_dir

    for infile_name in os.listdir(input_dir):
        infile = os.path.join(input_dir, infile_name)
        print "input: %s" % (infile)

        outfile_name = os.path.splitext(infile_name)[0] + '.pdf'
        outfile = os.path.join(output_dir, outfile_name)
        print "output: %s" % (outfile)

        try:
            image = Image.open(infile)
            image.save(outfile, 'PDF', resolution=100.0)
        except:
            continue
    
def concatpdf(input_dir, outfile):
    """Concatenate all the PDFs in input_dir into a single PDF.
    Writes the single PDF to outfile.  
    """
    outfile = outfile if outfile else 'concatpdf.pdf'

    merger = PdfFileMerger()
    for file in os.listdir(input_dir):
        if not os.path.splitext(file)[1] == '.pdf':
            continue
        print "Processing %s" % (file)
        infile = os.path.join(input_dir, file)
        merger.append(PdfFileReader(infile, 'rb'))
        print "Appended %s to %s" % (infile, outfile)

    merger.write(outfile)

def usage():
    print "images2pdf.py input_dir output_file"
    sys.exit(1)

def main():
    try:
        input_dir = sys.argv[1]
    except:
        usage()
    if not os.path.exists(input_dir):
        print "Path does not exist: %s" % (path)
        sys.exit(1)

    try:
        output_file = sys.argv[2] 
    except IndexError:
        # use the default output_file
        output_file = None

    # temp dir for generating intermediate pdfs
    try:
        tmpdir = tempfile.mkdtemp() 
        images2pdf(input_dir, tmpdir)
        concatpdf(tmpdir, output_file)
    except Exception, e:
        raise(e)
    finally:
        shutil.rmtree(tmpdir)
            
if __name__=="__main__":
    main()
