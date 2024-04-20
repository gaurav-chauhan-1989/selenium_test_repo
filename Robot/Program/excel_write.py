import openpyxl

wb=openpyxl.Workbook()
sh=wb.active
sh['A1'].value="Gaurav"
sh['B1'].value="abc123"
sh['A2'].value="Archana"
sh['B2'].value="ZXC123"
sh['A3'].value="Radhika"
sh['B3'].value="sdf890"
wb.save("E:\Sheet\write1.xlsx")

