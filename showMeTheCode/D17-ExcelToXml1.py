from openpyxl import load_workbook
import xml.etree.ElementTree as ET

wb = load_workbook(filename = 'student.xlsx')
sheet_ranges = wb['Sheet']
print(sheet_ranges['A1'].value)
print(sheet_ranges['B1'].value)
print(sheet_ranges['c3'].value)
dict = {}
for row in sheet_ranges:
    firstKey = row[0].value
    dict[firstKey] = []
    for i in range(1,len(row)):
        dict[firstKey].append(row[i].value)
print(dict)

# 保存修改了的xml
root = ET.Element("root")
students = ET.SubElement(root, "students")
students.insert(0,ET.Comment('''
	学生信息表
	"id" : [名字, 数学, 语文, 英文]'''))
students.text = str(dict)
tree = ET.ElementTree(root)
tree.write("filename.xml",encoding='UTF8')