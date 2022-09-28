import openpyxl

book = openpyxl.open("1111.xlsx", read_only = True)
sheet = book.active

cells = sheet["D1":"E8"]
for redemptionprice, basis in cells:
    print(redemptionprice.value, basis.value)

for row in range(1, 3):
    vidan = sheet[row][0].value
    dataPogasheniya = sheet[row][1].value
    price = sheet[row][2].value
    redemptionprice = sheet[row][3].value
    basis = sheet[row][4].value
    discount = sheet[row][5].value
    print(row, vidan, dataPogasheniya, price, redemptionprice, basis, discount)
