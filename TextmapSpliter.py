import os
import openpyxl

class Spliter(object):
    def Run(self, targetFile, maxRow):
        rowOneCellNames = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1"]
        book = openpyxl.load_workbook(targetFile, read_only=True)
        sheet = book[book.sheetnames[0]]
        sheet.max_row = maxRow
        columsName = []
        for i in rowOneCellNames:
            columsName.append(sheet[i].value)
        print(columsName)

if __name__ == "__main__":
    print("Begin ...")
    filename = "TextMapMerge去重-2.3 only-en.xlsx"
    maxRow = 38613
    #filename = "e1.xlsx"
    s = Spliter()
    s.Run(filename, maxRow)
    print("Done!")