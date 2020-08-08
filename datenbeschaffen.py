import csv
from datetime import datetime, timedelta

def abbringer(linien_text_abbringer, abbringer_ort):
    print("Funktion Abbringer wird ausgeführt")
    abbringer_zeiten = []
    with open('2020-07-31_istdaten.csv', newline='') as file:
        linereader = csv.reader(file, delimiter=';', quotechar='"')
    
        for line in linereader:
            if line[7] == linien_text_abbringer and line[13] == abbringer_ort:
                abfahrtszeit_str = line[17]
                ab_prognose_str = line[18]
                if abfahrtszeit_str:                 #Prüft ob die Zelle leer ist
                    abfahrtszeit = datetime.strptime(abfahrtszeit_str, "%d.%m.%Y %H:%M")
                else:
                    continue                               
                if ab_prognose_str:                 #Prüft ob die Zelle leer ist
                    ab_prognose = datetime.strptime(ab_prognose_str, "%d.%m.%Y %H:%M:%S")
                else:
                    continue
                abbringer_tupel = (abfahrtszeit, ab_prognose)
                abbringer_zeiten.append(abbringer_tupel)
        return abbringer_zeiten

def zubringer(linien_text_zubringer, zubringer_ort):
    print("Funktion Zubringer wird ausgeführt")
    zubringer_zeiten = []
    with open('2020-07-31_istdaten.csv', newline='') as file:
        linereader = csv.reader(file, delimiter=';', quotechar='"')

        for line in linereader:
            if line[7] == linien_text_zubringer and line[13] == zubringer_ort:
                ankunftszeit_str = line[14]
                an_prognose_str = line[15]
                if ankunftszeit_str:                 #Prüft ob die Zelle leer ist
                    ankunftszeit = datetime.strptime(ankunftszeit_str, "%d.%m.%Y %H:%M")
                else:
                    continue                               
                if an_prognose_str:                 #Prüft ob die Zelle leer ist
                    an_prognose = datetime.strptime(an_prognose_str, "%d.%m.%Y %H:%M:%S")
                else:
                    continue
                zubringer_tupel = (ankunftszeit, an_prognose)
                zubringer_zeiten.append(zubringer_tupel)
        return zubringer_zeiten
