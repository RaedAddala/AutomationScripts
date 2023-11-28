from PyPDF2 import PdfMerger, PdfReader
from sys import argv


merger = PdfMerger()

outputFileName = None


for arg in argv[1:]:
    if(arg == '-o'):
        if(argv.index(arg) + 1 >= len(argv)):
            print('Error: No output file name specified')
            exit()
        outputFileName = argv[argv.index(arg) + 1]
        merger.write(outputFileName)
        print("Merged output file: " + outputFileName)
        exit()
    try:
      if(arg.endswith('.pdf') == False):
        raise Exception("file {argv} is not a pdf file")
      
      pdfFile = open(arg, 'rb')
      merger.append(PdfReader(pdfFile))
    except Exception as e:
      print(e)
      exit()
else:
  merger.write("output.pdf")
  print("Merged output file: output.pdf")
        