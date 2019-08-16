from openpyxl import load_workbook
import xml.etree.ElementTree as ET

#student.xlsx is the out put of D16
wb = load_workbook(filename = 'city.xlsx')
sheet_ranges = wb['Sheet']
print(sheet_ranges.max_row)