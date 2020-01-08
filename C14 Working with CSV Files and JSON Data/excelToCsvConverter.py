#! python3
# Converts excel files to csv format in current working directory,

import os, openpyxl, csv

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue

    print("Working with excel file: " + excelFile + "...")
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        print("Working with sheet: " + sheetName + "...")
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]

        # Create the CSV filename from the Excel filename and sheet title.
        splitName = excelFile.split(".")    # split string using '.' as separat.
        csvFileName = splitName[0] + "_" + sheetName + ".csv"
        
        csvFile = open(csvFileName, 'w', newline='')
        # Create the csv.writer object for this CSV file.
        csvWriter = csv.writer(csvFile)

        # Loop through every row in the sheet.
        print("Writing to " + csvFileName + "...")
        for rowNum in range(1, sheet.max_row + 1):
            rowData = [] # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)

            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)

        csvFile.close()
print("Done")