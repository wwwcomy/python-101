from openpyxl import load_workbook
import xml.etree.ElementTree as ET

#city.xlsx is the out put of D15
wb = load_workbook(filename = 'city.xlsx')
sheet_ranges = wb['Sheet']
dict = {}
for row in sheet_ranges:
    dict[row[0].value] = row[1].value
print(dict)

# 保存修改了的xml
root = ET.Element("root")
cities = ET.SubElement(root, "cities")
cities.insert(0,ET.Comment('''
	城市信息
	'''))
cities.text = str(dict)
tree = ET.ElementTree(root)
tree.write("city.xml",encoding='UTF8')