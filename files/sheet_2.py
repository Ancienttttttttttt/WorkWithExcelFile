import openpyxl

book = openpyxl.open("1111.xlsx", read_only = True)
sheet_2 = book.worksheets[2]
print(sheet_2)

cells = sheet_2["A3":"B15"]
for Baseline, values in cells:
    print(Baseline.value, values.value)