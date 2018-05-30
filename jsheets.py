import gspread
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials
import re
from wordcloud import WordCloud


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('my_secret.json', scope)

gc = gspread.authorize(credentials)
BASIC_DELIM = '\s|;|,|\n|[()]|\r'
COMMON = ['at', 'an', 'the', 'and', 'with', 'is', 'in', 'between', 'not']


ws = gc.open("The Bar - Template")


def worksheet2words(worksheet, sRange, cRange, delimiters):
    words = list()
    for i in sRange:
        sheet = worksheet.get_worksheet(i)
        for cell in sheet.range(cRange):
            words.extend(re.split(delimiters,cell.value))
    return list(filter(None, words))

def freqTable(words):
    d = dict()
    for word in words:
        word = word.lower()
        if word not in d:
            d[word] = 1
        else: d[word] += 1
    return d

def filterWords(frt):
    d = dict()
    for word in frt.keys():
        if word not in COMMON:
            d[word] = frt[word]
    return d


def displayWordcloud(words):
    frt = filterWords(freqTable(words))
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate_from_frequencies(frt)
    
    # plot the WordCloud image                       
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()



sRange = range(1,5)
cRange = "C3:I3"
oRange = "C5:I5"
words = worksheet2words(ws, sRange, cRange, BASIC_DELIM)
displayWordcloud(words)
displayWordcloud(worksheet2wrods(gc.open(), sRange, oRange, BASIC_DELIM))
