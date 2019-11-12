#! python3
# decrypts pdfs in given directory and its subdirectories using a password
# provided in command line argument

import sys, os, PyPDF2

if(len(sys.argv) != 2):
    print("Invalid number of arguments")
    sys.exit(1)

for foldername, subfolders, filenames in os.walk('.'):
    path = os.path.abspath(foldername)
    print("Processing folder: " + path + "...")
    for filename in filenames:
        if filename.endswith("_encrypted.pdf"):
            print("Processing file: " + filename + "...")
            newFile = os.path.join(path, filename)
            pdfFileObj = open(newFile, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            if pdfReader.isEncrypted:
                print("File " + filename + " is encrypted")
                if not pdfReader.decrypt(sys.argv[1]):
                    print("Password for " + filename + " is incorrect")
                    continue
                print ("Provided password is correct!")
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                resultFileName = filename.split("_encrypted.pdf")[0] + ".pdf"
                resultFile = os.path.join(path, resultFileName)
                resultPdf = open(resultFile, 'wb')
                print("Creating " + resultFileName + "...")
                pdfWriter.write(resultPdf)
                resultPdf.close()
                pdfFileObj.close()
        else:
            continue
    print()
print("Done")