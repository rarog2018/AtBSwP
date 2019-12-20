#! python3
# performs a brute-force attack on a PDF file

# 1. Check the validity of command line arguments
#   a) check the number of arguments
#   b) check if the argument is a PDF 
#   c) check if the file exists
# 2. Read the dictionary (we assume that it is a part of the program)
# 3. Prepare PDF Reader Object
# 4. Loop through each line and pass it as an argument to the decrypt() method
# in both uppercase and lowercase
#   a) check if uppercase fails:
#       check if lowercase fails:
#           proceed next word (continue)
#       else update password variable and break
#   b) else update password variable and break
# 5. Check the contents of password variable:
#   a) if it is not empty print success
#   b) if it is empty print that password was not found

import PyPDF2, sys, os

# 1. Check the validity of command line arguments
#   a) check the number of arguments
if(len(sys.argv) != 2):
    print("Invalid number of arguments")
    sys.exit(1)

#   b) check if the argument is a PDF 
if not sys.argv[1].endswith(".pdf"):
    print("Given file is not a PDF file")
    sys.exit(1)

#   c) check if the file exists
if not os.path.isfile(os.path.join(os.getcwd(), sys.argv[1])):
    print("File does not exist")
    sys.exit(1)
    
filePath = os.path.join(os.getcwd(), sys.argv[1])
    
# 2. Read the dictionary (we assume that it is a part of the program)
dictFile = open("./dictionary.txt")
dictionary = dictFile.readlines()

# 3. Prepare PDF Reader Object
pdfFileObj = open(filePath, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# 4. Loop through each word and pass it as an argument to the decrypt() method
# in both uppercase and lowercase
password = ""
for word in dictionary:
    print(word.rstrip())
    #   a) check if uppercase fails:
    if not pdfReader.decrypt(word.rstrip()):
        print(word.lower().rstrip())
        #       check if lowercase fails:
        if not pdfReader.decrypt(word.lower().rstrip()):
            #           proceed next word (continue)
            continue
        #       else update password variable and break
        else:
            password = word.lower().rstrip()
            break
    #   b) else update password variable and break
    else:
        password = word.rstrip()
        break
    
# 5. Check the contents of password variable:
#   a) if it is not empty print success
if password:
    print("Success! The password was: " + password)
#   b) if it is empty print that password was not found
else:
    print("Fail! The password was not found.")

print("Done")
