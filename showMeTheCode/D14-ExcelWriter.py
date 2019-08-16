from openpyxl import Workbook
dict = {}
try:
    with open("student.txt","r") as student:
        content = student.read()
        dict = eval(content)
        print(content)
        print(dict)
except IOError as err:
    print(str(err))

print(dict['1'])

wb = Workbook()

# grab the active worksheet
ws = wb.active

arr = []
for key in dict:
    arr.clear()
    arr.append(key)
    arr.extend(dict.get(key))
    # Rows can also be appended
    ws.append(arr)

# Save the file
wb.save("student.xlsx")