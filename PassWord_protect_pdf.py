from PyPDF2 import PdfFileReader, PdfFileWriter
import getpass
pdfwriter=PdfFileWriter()
pdf=PdfFileReader(open("Name_of_pdf.pdf","rb"))
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
passw=getpass.getpass(prompt='Enter password: ')
pdfwriter.encrypt(passw)
name=input("Enter the name of the file: ")
with open(name,'wb') as f:
    pdfwriter.write(f)