#! python3
# encrypts pdfs in given directory and its subdirectories using a password
# provided in command line argument

# 1. Check the validity of command line arguments
# 2. Go through every pdf in the cwd and its subfolders
#   a) save the path and prompt info
#   b) prepare the file in reading mode
#   c) check if file is encrypted
#       if it ends with our ending continue
#       if not copy the file and change the name so that it has our ending
#   d) if file is not encrypted  
#       prepare writer
#       copy the contents of the processed pdf
#       encrypt the pdf
#       create new pdf file
#       write copied contents into newly created file
#       check if new file is encrypted
#           try to read the page if it is
#           delete the original file
#       report failure if newfile is not encrypted
#   e) new line for visual purposes

import sys, os, PyPDF2, shutil

# 1. Check the validity of command line arguments
if(len(sys.argv) != 2):
    print("Invalid number of arguments")
    sys.exit(1)

# 2. Go through every pdf in the cwd and its subfolders
for foldername, subfolders, filenames in os.walk('.'):
    # save the path and prompt info
    path = os.path.abspath(foldername)
    print("Processing folder: " + path + "...")
    for filename in filenames:
        if filename.endswith(".pdf"):
            print("Processing file: " + filename + "...")
            # prepare the file in reading mode
            pdfFileObj = open(os.path.join(path, filename), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            # check if file is encrypted
            if pdfReader.isEncrypted:
                pdfFileObj.close()
                print(filename + " is already encrypted")
                # if it ends with our ending continue
                if filename.endswith("_encrypted.pdf"):
                    continue
                # if not copy the file and change the name so that it has
                # "_encrypted.pdf" ending
                else:
                    shutil.move(os.path.join(path, filename), os.path.join(path, (filename.split('.pdf')[0] + "_encrypted.pdf")))    
            # if file is not encrypted    
            else:
                # prepare writer
                pdfWriter = PyPDF2.PdfFileWriter()
                # copy the contents of the processed pdf
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                # encrypt the pdf
                pdfWriter.encrypt(sys.argv[1], sys.argv[1])
                # create new pdf file
                newFileName = filename.split('.pdf')[0] + "_encrypted.pdf"
                newFile = os.path.join(path, newFileName)
                resultPdf = open(newFile, 'wb')
                # write copied contents into newly created file
                pdfWriter.write(resultPdf)
                resultPdf.close()

                # check if new file is encrypted
                newpdfFileObj = open(newFile, 'rb')
                newpdfReader = PyPDF2.PdfFileReader(newpdfFileObj)
                if newpdfReader.isEncrypted:
                    if not newpdfReader.decrypt(sys.argv[1]):
                        print("Password for " + newFileName + " is incorrect")
                        continue
                    # try to read the page
                    try:
                        newpdfReader.getPage(0)
                    except PyPDF2.utils.PdfReadError as err:
                        print(newFileName + " " + str(err))
                        continue
                    print(newFileName + " has been succesfully encrypted!")
                    # delete the original file
                    pdfFileObj.close()
                    print("Deleting " + filename + "...")
                    os.unlink(os.path.join(path, filename))
                # report failure if file is not encrypted
                else:
                    print("Failed to encrypt " + newFileName)
    # new line for visual purposes
    print()
print("Done")
