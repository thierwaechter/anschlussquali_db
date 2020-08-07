import csv
from datetime import datetime

def abbringer(linien_text_abbringer, abbringer_ort):
    print("Funktion Abbringer wird ausgeführt")
    abbringer_zeiten = []
    with open('2020-07-31_istdaten.csv', newline='') as file:
        linereader = csv.reader(file, delimiter=';', quotechar='"')
    
        for line in linereader:
            if line[7] == linien_text_abbringer and line[13] == abbringer_ort:
                ab_prognose_str = line[17]
                abbringer_zeiten.append(ab_prognose_str)
        return ab_prognose_str

def zubringer(linien_text_zubringer, zubringer_ort):
    print("Funktion Zubringer wird ausgeführt")
    zubringer_zeiten = []
    with open('2020-07-31_istdaten.csv', newline='') as file:
        linereader = csv.reader(file, delimiter=';', quotechar='"')

        for line in linereader:
            if line[7] == linien_text_zubringer and line[13] == zubringer_ort:
                an_prognose_str = line[15]
                zubringer_zeiten.append(an_prognose_str)
        return zubringer_zeiten
