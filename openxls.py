import openpyxl, pprint, csv
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

diffCount = 0
print("Loading file...")
with open('diffproducts.csv', 'w',newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    for rowOfCellObjects in sheet['A1':'B12775']:
        if rowOfCellObjects[0].value != rowOfCellObjects[1].value:
           filewriter.writerow([rowOfCellObjects[0].value, rowOfCellObjects[1].value])
           diffCount += 1
    
print("Done.")
print(diffCount)


