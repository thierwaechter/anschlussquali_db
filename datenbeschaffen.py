import csv
from datetime import datetime

with open('2020-07-31_istdaten.csv', newline='') as file:
    linereader = csv.reader(file, delimiter=';', quotechar='"')

    def abbringer(linien_text_zubringer, zubringer_ort):
        for line in linereader:
            if line[7] == linien_text_zubringer and line[13] == zubringer_ort:
                an_prognose_str = line[15]
                return an_prognose_str

    def zubringer(linien_text_abbringer, abbringer_ort):
        for line in linereader:
            if line[7] == linien_text_abbringer and line[13] == abbringer_ort:
                ab_prognose_str = line[17]
                return ab_prognose_str