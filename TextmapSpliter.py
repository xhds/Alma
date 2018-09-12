import os
import openpyxl
import datetime
import sys

class Spliter(object):
    def Run(self, targetFile, maxRow = 0):
        rowOneCellNames = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1"]
        book = openpyxl.load_workbook(targetFile, read_only=True)
        sheet = book[book.sheetnames[0]]
        if maxRow != 0:
            sheet.max_row = maxRow
        columsName = []
        for i in rowOneCellNames:
            columsName.append(sheet[i].value)
        
        rowIndex = 1
        maxIndex = sheet.max_row
        allData = {}
        isFirstRow = True
        for row in sheet:

            sys.stdout.write("processing index %d/%d \r" %(rowIndex, maxIndex))
            sys.stdout.flush()
            rowIndex += 1

            if isFirstRow:
                isFirstRow = False
                continue
            rowData = None
            rowID = ""
            oneRow = []
            for cell in row:
                if rowData == None:
                    rowID = cell.value
                    if rowID == None:
                        break
                    rowData = allData.get(rowID)
                    if rowData == None:
                        rowData = []
                        allData[rowID] = rowData
                oneRow.append(cell.value)
            if rowData != None:
                rowData.append(oneRow)
        print("\n process Done!")
        
        print("Begin write files")
        fileIndex = 1
        maxFile = len(allData)
        for fileName in allData:
            if fileName == None:
                continue
            sys.stdout.write("processing file %d/%d \r" %(fileIndex, maxFile))
            sys.stdout.flush()
            fileIndex += 1

            writeBook = openpyxl.Workbook(write_only=True)
            writeSheet = writeBook.create_sheet()
            writeSheet.append(columsName)
            for row in allData[fileName]:
                writeSheet.append(row)
            writeBook.save(fileName+".xlsx")
        print("\n Write Done!")

if __name__ == "__main__":
    print("Begin ... at %s " % datetime.datetime.now())
    filename = "TextMapMerge去重-2.3 only-en.xlsx"
    maxRow = 38615
    s = Spliter()
    s.Run(filename, maxRow)
    print("Done! at %s " % datetime.datetime.now())