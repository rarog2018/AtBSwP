#! python3
# Generates an invitation for each name in a guests.txt file

# 1. Check the validity of the text file
#   a) check if the text file exists
#   b) check if it is not empty
# 2. Read the text file line by line
#   a) add each line to a list of names
# 3. Prepare the text of the document
#   a) create a list with custom text and 'name' to be replaced
# 4. Prepare the document itself
#   a) create a document object
#   b) for every name in name list:
#       add paragraph and style it
#       if there are names left add break

import sys, docx, os.path

def style_text(paraObj, fontName, size=20, run=0, boldness=False, undrln=False):
    run = paraObj.runs[run]   # create run object
    font = run.font         # and font object for this run object
    font.name = fontName    # set font name
    font.size = docx.shared.Pt(size)  # set font size
    font.bold = boldness
    font.underline = undrln

# 1. Check the validity of the text file
#   a) check if the text file exists
fpath = os.getcwd() + "/guests.txt"
if not os.path.isfile(fpath):
    print("guests.txt is not in the current working directory")
    sys.exit(1)

#   b) check if it is not empty
if not os.path.getsize(fpath):
    print("guests.txt is empty")
    sys.exit(1)

# 2. Read the text file line by line
#   a) add each line to a list of names
names = []
guestFile = open(fpath, 'r')
names = guestFile.readlines()
guestFile.close()

# 3. Prepare the text of the document
#   a) create a list with custom text and 'name' to be replaced
textLst = [["It would be a pleasure to have the company of"], ["name"], 
    ["at", " 11010 Memory Lane on the Evening of"], ["April 1st"], 
    ["at", " 7 o'clock"]]

# 4. Prepare the document itself
#   a) create a document object
doc = docx.Document()
doc.save("invitations.docx")

#   b) for every name in name list:
for name_n in range(len(names)):
    print("Working with " + names[name_n].rstrip() + "...")
    #       add paragraph and style it
    for line_n in range(len(textLst)):
        print("Adding line " + str(line_n + 1) + "...")
        # check if the element that we work on is a placeholder for name
        if textLst[line_n][0] == "name":
            # replace it with name that we work on
            paraObj = doc.add_paragraph(names[name_n].rstrip(), 'Normal')
            # set font style to "TNR" and size to 21, run 0, bold=True
            style_text(paraObj, "Times New Roman", 18, 0, True)
        else:
            paraObj = doc.add_paragraph(textLst[line_n][0], 'Normal')
            # for each even line
            if not line_n % 2:
                # set font style to "BSS"
                style_text(paraObj, "Brush Script Std")
                if line_n != 0:
                    # for lines 2, 4 set run 0 underline to True
                    style_text(paraObj, "Brush Script Std", 20, 0, False, True)
            # for each uneven line
            else:
                style_text(paraObj, "Times New Roman", 18)

        # adjust paragraph alignment to center
        paraObj.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
        if len(textLst[line_n]) > 1:
            # adding other run objects to paragraphs
            for run_n in range(1, len(textLst[line_n])):
                print("Adding run " + str(run_n) + "...")
                paraObj.add_run(textLst[line_n][run_n])
                if not line_n % 2:
                    style_text(paraObj, "Brush Script Std", 20, run_n)

    #       if there are names left add break
    if name_n:
        doc.paragraphs[len(doc.paragraphs) - (len(textLst)+1)].runs[1].add_break(docx.enum.text.WD_BREAK.PAGE)

doc.save("invitations.docx")
print("Done")
