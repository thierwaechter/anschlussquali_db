from datetime import datetime, timedelta
from datenbeschaffen import holeabbringerzeit, holezubringerzeit

auswertung_2870 = {}

#Abbringer Angaben Anschluss 2870
linien_text_abbringer = '160'  # wird in def holeabbringerzeit verwendet
abbringer_ort = 'Münsingen Bahnhof'  # wird in def holezabbringerzeit verwendet
abfahrt1 = '00:05:00'
abfahrt2 = '00:35:00'

#Umsteigezeit Anschluss 2870
min_umsteigezeit = timedelta(minutes=2)
max_umsteigezeit1 = timedelta(minutes=15) # Für Ankunft 01
max_umsteigezeit2 = timedelta(minutes=6) # Für Ankunft 31

# Zubringer filtern nach definierten Anschlüssen, gemäss ankunft1 und anfunft2
def anschluss_2870():
    an_temp_tabelle1 = []
    an_temp_tabelle2 = []

#Zubringer Angaben Anschluss 2870
    linien_text_zubringer = 'S1' # wird in def holezubringerzeit verwendet
    zubringer_ort = 'Münsingen'  # wird in def holezubringerzeit verwendet
    ankunft1_str = '31.07.2020 06:01' 
    ankunft1 = datetime.strptime(ankunft1_str, '%d.%m.%Y %H:%M') 
    ankunft2_str = '31.07.2020 06:31'
    ankunft2 = datetime.strptime(ankunft2_str, '%d.%m.%Y %H:%M') 

    liste_zubringer_zeiten = holezubringerzeit(linien_text_zubringer, zubringer_ort)
    liste_abbringer_zeiten = holeabbringerzeit(linien_text_abbringer, abbringer_ort)        

    # Erste Tagzeit abgleichen und in temporäre Tabelle schreiben
    print('Erste Tagzeit abgleichen in Tabelle schreiben')
    for i in range(15):
        for ankunftszeit in liste_zubringer_zeiten:
            if  ankunftszeit[0] == ankunft1:
                an_temp_tabelle1.append(ankunftszeit)
        ankunft1 = ankunft1 + timedelta(hours=1)

    # Erste Tagzeit anhand der temporären Tabelle Anschlüsse suchen und Haupttabelle schreiben
    print('Erste Tagzeit auswerten und in die Auswertung schreiben')
    for an_zeit in an_temp_tabelle1:
        for ab_zeit in liste_abbringer_zeiten:
            if ab_zeit[1] >= an_zeit[1] + min_umsteigezeit and ab_zeit[1] <= an_zeit[1] + max_umsteigezeit1:
                auswertung_2870[an_zeit] = ab_zeit
                break      
            else: 
                auswertung_2870[an_zeit] = 0

    # Zweite Tagzeit abgleichen und in temporäre Tabelle schreiben
    print('Zweite Tagzeit abgleichen in Tabelle schreiben')
    for i in range(14):
        for ankunftszeit in liste_zubringer_zeiten:
            if  ankunftszeit[0] == ankunft2:
                an_temp_tabelle2.append(ankunftszeit)
        ankunft2 = ankunft2 + timedelta(hours=1)

    # Zweite Tagzeit anhand der temporären Tabelle Anschlüsse suchen und in Haupttabelle schreiben
    print('Zweite Tagzeit auswerten und in die Auswertung schreiben')
    for an_zeit in an_temp_tabelle2:
        for ab_zeit in liste_abbringer_zeiten:
            if ab_zeit[1] >= an_zeit[1] + min_umsteigezeit and ab_zeit[1] <= an_zeit[1] + max_umsteigezeit2:
                auswertung_2870[an_zeit] = ab_zeit
                break      
            else: 
                auswertung_2870[an_zeit] = 0

    # Prozentsatz gefundener Anschlüsse zu definierter Anschlüsse berechnen
    # anzahl_def_anschluesse = len(an_temp_tabelle1) + len(an_temp_tabelle2)
    #anzahl_OK_anschluesse = len(auswertung_2870['Anschluss 2870'])
    #prozent_2870 = anzahl_OK_anschluesse / anzahl_def_anschluesse * 100

    #print('Von ' + str(anzahl_def_anschluesse) + ' wurden ' + str(anzahl_OK_anschluesse) + ' gehalten.')
    #print('Das sind ' + str(prozent_2870) + '%.')
    print(auswertung_2870)
    return auswertung_2870
