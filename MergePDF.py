import PyPDF2 as PP

def merge(file1, file2):
    '''This function merges two pdfs together'''
    
    # creating a shell for the merged file
    mergedpdfobj = PP.PdfFileWriter()    
 
    # opening the pdfs
    pdf1File = open(file1, 'rb')
    pdf2File = open(file2, 'rb')
    
    # reading pdfs
    pdf1Reader = PP.PdfFileReader(pdf1File)
    pdf2Reader = PP.PdfFileReader(pdf2File)
   
    # adding file1 to mergedPDF
    for page_num1 in range(pdf1Reader.numPages):
        page = pdf1Reader.getPage(page_num1)
        mergedpdfobj.addPage(page)

    # adding file2 to mergedPDF
    for page_num2 in range(pdf2Reader.numPages):
        page = pdf2Reader.getPage(page_num2)
        mergedpdfobj.addPage(page)

    # creating the mergePDF file
    mergedpdfname = str(input('Merge PDFs as: '))
    mergedpdf = open('{}.pdf'.format(mergedpdfname), 'wb')
    mergedpdfobj.write(mergedpdf)

    # closing all Files
    pdf1File.close()
    pdf2File.close()
    mergedpdf.close()

    return 'PDFs merged as {}.pdf'.format(mergedpdfname)
    
