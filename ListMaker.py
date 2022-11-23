from codecs import utf_8_decode
from pkgutil import get_data
from sre_compile import isstring
import yahoo_fin.stock_info as si
from yahoo_fin import options

f1 = open("E:\!Development\SR List Maker\input.txt","rt", encoding="utf8")
f2 = open("E:\!Development\SR List Maker\output.txt","w+", encoding="utf8")

data = f1.read()
words = data.split()
tickers = []

for i in words:
    if(len(i) > 1):
        if(i[0] == '$' and (i[1] < '0' or i[1] > '9') and i[1] != '('):
            i = i.replace(')','')
            i = i.replace('-','')
            i = i.replace(':','')
            tickers.append(i)

tickers = list(dict.fromkeys(tickers))

for i in tickers:

    f2.write(i)
    t = i
    t = t[1:]
    ticker = si.get_quote_data(t)
    # print(ticker)

    temp1 = float(ticker["regularMarketChange"])
    temp1 = round(temp1,4)
    # print(temp1)

    temp2 = float(ticker["regularMarketPreviousClose"])
    temp2 = round(temp2,4)
    # print(temp2)

    percent = ((temp1*100)/temp2)
    percent = round(percent,2)

    f2.write("\t")
    f2.write(str(percent))
    f2.write("%")
    f2.write("\n")