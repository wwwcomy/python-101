from openpyxl import Workbook
dict = []
try:
    with open("numbers.txt","r") as numbers:
        content = numbers.read()
        dict = eval(content)
except IOError as err:
    print(str(err))

print(dict)
print(dict[0])
print(dict[0][0])

wb = Workbook()

# grab the active worksheet
ws = wb.active

for row in dict:
    ws.append(row)

# Save the file
wb.save("D16-numbers.xlsx")