#! python3
# takes two integers and a filename string as command line arguments
# Starting at row N, the program should insert M blank rows into the spreadsheet.

import sys, openpyxl

# check if the number of arguments is valid
if(len(sys.argv) != 4):
    print("Invalid number of arguments")
    sys.exit(1)

# check if second and third arguments are integers
nArg, mArg = sys.argv[1], sys.argv[2]

try:
    N, M = int(nArg), int(mArg)
except ValueError as err:
    print("Unable to parse argument as an integer: " + str(err))
    sys.exit(1)

# load workbook
try:
    wb = openpyxl.load_workbook(sys.argv[3])
except FileNotFoundError as err:
    print(str(err))
sheet = wb.active

# open and set up new workbook
nw = openpyxl.Workbook()
ns = nw.active
ns.title = sheet.title

# write first part of the source workbook into new workbook
for irow in range(1, N):
    for jcol in range(1, sheet.max_column + 1):
        ns.cell(row=irow, column=jcol).value = sheet.cell(
            row=irow, column=jcol).value

# write second part of the source workbook into new workbook
for irow in range(N + M, sheet.max_row + M + 1):
    for jcol in range(1, sheet.max_column + 1):
        ns.cell(row=irow, column=jcol).value = sheet.cell(
            row=irow - M, column=jcol).value

# save to a new file
nw.save("new" + str(sys.argv[3]))
print("Done")
