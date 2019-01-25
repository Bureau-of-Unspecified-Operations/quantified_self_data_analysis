from jsheets import *

sRange = range(1,5)
joy = "C3:I3"
above = "C4:I4"
pain = "C5:I5"
under = "C6:I6"

allSheets = ["The Bar- Dec/Jan", "The Bar - Feb", "Bar:Mar", "The Bar: Mar-Apr", "The Bar - April"]


def makeCloudFromWorksheets(sheets, sRange, cRange):
    gc = setup()
    words = list()
    for sheet in sheets:
        words.extend(worksheet2words(gc.open(sheet), sRange, cRange, BASIC_DELIM))
    displayWordcloud(words)




makeCloudFromWorksheets(allSheets, sRange, under)
makeCloudFromWorksheets(allSheets, sRange, joy)
makeCloudFromWorksheets(allSheets, sRange, above)

