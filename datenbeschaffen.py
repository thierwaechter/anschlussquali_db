import csv
from datetime import datetime, timedelta

def abbringer(linien_text_abbringer, abbringer_ort):
    print("Funktion Abbringer wird ausgeführt")
    abbringer_zeiten = []
    with open('2020-07-31_istdaten.csv', newline='') as file:
        linereader = csv.reader(file, delimiter=';', quotechar='"')
    
        for line in linereader:
            if line[7] == linien_text_abbringer and line[13] == abbringer_ort:
                ab_prognose_str = line[18]
                if ab_prognose_str:
                    ab_prognose = datetime.strptime(ab_prognose_str, "%d.%m.%Y %H:%M:%S")
                    abbringer_zeiten.append(ab_prognose)
                else:
                    pass
        return abbringer_zeiten

def zubringer(linien_text_zubringer, zubringer_ort):
    print("Funktion Zubringer wird ausgeführt")
    zubringer_zeiten = []
    with open('2020-07-31_istdaten.csv', newline='') as file:
        linereader = csv.reader(file, delimiter=';', quotechar='"')

        for line in linereader:
            if line[7] == linien_text_zubringer and line[13] == zubringer_ort:
                an_prognose_str = line[15]
                if an_prognose_str:
                    an_prognose = datetime.strptime(an_prognose_str, "%d.%m.%Y %H:%M:%S")
                    zubringer_zeiten.append(an_prognose)
                else:
                    pass
        return zubringer_zeiten
