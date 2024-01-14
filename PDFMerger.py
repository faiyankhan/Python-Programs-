import PyPDF2

pdfFiles = ["Certificate1.pdf","Certificate2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfFiles:
        pdfFiles = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFiles)
        merger.append(pdfReader)
pdfFiles.close()
merger.write('merged.pdf')