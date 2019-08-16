from openpyxl import Workbook
dict = {}
try:
    with open("city.txt","r") as city:
        content = city.read()
        dict = eval(content)
except IOError as err:
    print(str(err))

print(dict)

wb = Workbook()

# grab the active worksheet
ws = wb.active

arr = []
for key in dict:
    arr.clear()
    arr.append(key)
    arr.append(dict.get(key))
    # Rows can also be appended
    ws.append(arr)

# Save the file
wb.save("D15-city.xlsx")