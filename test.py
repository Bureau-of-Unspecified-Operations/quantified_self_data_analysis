import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('my_secret.json', scope)

gc = gspread.authorize(credentials)

sht = gc.open("The Bar - Template")
worksheets = list()


over = list()
joy = list()
pain = list()
under = list()
for worksheet in worksheets:
    joy.extend(worksheet.range('C3:I3'))
    over.extend(worksheet.range('C4:I4'))
    pain.extend(worksheet.range('C5:I5'))
    under.extend(worksheet.range('C6:I6'))

for cell in joy:
    print(cell.value + "\n\nthings\n\n")


def sheet2Strings(sheet, over, joy, pain, under):
    sheet = list()
    for i in range(1,5):
        sheets.append(sheet.get_worksheet(i))


def cellsFromSheet(sheet, cellRanges, buckets):
    for i, cellRange in enumerate(cellRanges):
        buckets[i].extend(sheet.range(cellRange))

def cellsFromWorksheet(worksheet, sheetRange, cellRanges, buckets):
    for i in sheetRange:
        cellsFromSheet(worksheet.get_worksheet(i), cellRanges, buckets)

def strListFromCells(cells, strList):
    delimiters = 
    for cell in cells:
        strList.extend(re.split(delimiters,cell)

def cellsFromMultipleWorksheets(sheetList,  sheetRange, cellRanges, buckets):
    for worksheet in sheetList:
        cellsFromWorksheet(worksheet, sheetRange, cellRanges, buckets)

def makeTXT():
    for key in words.keys():
        if word in common:
        

        