import PyPDF2 as PP

def cut(file1,initpage,finalpage):
    '''This function cuts pages from a pdf'''
    
    # creating a shell for the new file
    cutpdfobj = PP.PdfFileWriter()    
 
    # opening the pdf
    pdf1File = open(file1, 'rb')
    
    # reading the pdf
    pdf1Reader = PP.PdfFileReader(pdf1File)
   
    # verifying page validity
    try:
        assert initpage in range(1,pdf1Reader.numPages+1)\
            and finalpage in range(pdf1Reader.numPages)
    except AssertionError:
        return 'Error: please enter valid page numbers'

    # adding file1 to cutPDF
    for page_num1 in range(initpage-1,finalpage):
        page = pdf1Reader.getPage(page_num1)
        cutpdfobj.addPage(page)


    # creating the cutPDF file
    cutpdfname = str(input('Cut PDFs as: '))
    cutpdf = open('{}.pdf'.format(cutpdfname), 'wb')
    cutpdfobj.write(cutpdf)

    # closing all Files
    pdf1File.close()
    cutpdf.close()

    return 'cut PDF as {}.pdf'.format(cutpdfname)
    
