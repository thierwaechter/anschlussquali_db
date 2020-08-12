from datetime import datetime, timedelta
import csv
# from datenbeschaffen import Abbringerzeiten, Zubringerzeiten

def anschluss(anschlussnummer):
    if anschlussnummer == '2870':
        return anschluss_2870()
    if anschlussnummer == '2871':
        return anschluss_2871()
    if anschlussnummer == '2872':
        return anschluss_2872()

class Zubringer():
    def __init__(self, zubringer_linien_text, zubringer_haltestellen_name):
        self.zubringer_linien_text = zubringer_linien_text
        self.zubringer_haltestellen_name = zubringer_haltestellen_name

    def holezubringerzeit(self):
            print("Daten Zubringer werden gesucht...")
            zubringer_zeiten = []
            with open('2020-07-31_istdaten.csv', newline='') as file:
                linereader = csv.reader(file, delimiter=';', quotechar='"')
                for line in linereader:
                    if line[7] == self.zubringer_linien_text and line[13] == self.zubringer_haltestellen_name:
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
                        if ankunftszeit_str:
                            zubringer_tupel = (ankunftszeit, an_prognose)
                            zubringer_zeiten.append(zubringer_tupel)
                        else: 
                            continue
                print(len(zubringer_zeiten))        
                return zubringer_zeiten


class Abbringer():
    def __init__(self, abbringer_linien_text, abbringer_haltestellen_name):
        self.abbringer_linien_text = abbringer_linien_text
        self.abbringer_haltestellen_name = abbringer_haltestellen_name

    def holeabbringerzeit(self):
        print("Daten Abbringer werden gesucht...")
        abbringer_zeiten = []
        with open('2020-07-31_istdaten.csv', newline='') as file:
            linereader = csv.reader(file, delimiter=';', quotechar='"')
            for line in linereader:
                if line[7] == self.abbringer_linien_text and line[13] ==  self.abbringer_haltestellen_name:
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
            print(len(abbringer_zeiten))
            return abbringer_zeiten


class Anschluss():
    def __init__(self, name, ankunft_str, abfahrt_str, min_umsteigezeit_int, max_umsteigezeit_int):
        self.__anschluesse = {}
        self.name = name
        self.ankunft_str = ankunft_str
        self.abfahrt_str = abfahrt_str
        self.min_umsteigezeit_int = min_umsteigezeit_int
        self.max_umsteigezeit_int = max_umsteigezeit_int

        self.min_umsteigezeit = timedelta(minutes=self.min_umsteigezeit_int)
        self.max_umsteigezeit = timedelta(minutes=self.max_umsteigezeit_int)
        self.ankunft = datetime.strptime(self.ankunft_str, '%d.%m.%Y %H:%M')


    def zubringerzeit_filtern(self, liste_zubringer_zeiten):
        print('Zubringer aus Haupttabelle filtern und in temporäre Tabelle schreiben...')
        an_temp_tabelle = []
        for i in range(15):  #ACHTUNG 15 ist noch eine feste Variable! Noch anpassen!
            for ankunftszeit in liste_zubringer_zeiten:
                if  ankunftszeit[0] == self.ankunft:
                    an_temp_tabelle.append(ankunftszeit)
            self.ankunft = self.ankunft + timedelta(hours=1)
        print(len(an_temp_tabelle))
        return an_temp_tabelle

    def anschluss_suchen(self, an_temp_tabelle, liste_abbringer_zeiten):
        print('Von temporärer Tabelle passende Anschlüsse suchen...')
        auswertung = {}
        for an_zeit in an_temp_tabelle:
            for ab_zeit in liste_abbringer_zeiten:
                if ab_zeit[1] >= an_zeit[1] + self.min_umsteigezeit and ab_zeit[1] <= an_zeit[1] + self.max_umsteigezeit:
                    auswertung[an_zeit] = ab_zeit
                    break      
                else: 
                    auswertung[an_zeit] = 0
        print(auswertung)
        return auswertung


#bn = Bern, th = Thun, s1 = LINIEN_TEXT
bn_th_s1 = Zubringer('S1', 'Münsingen')

#ms = Münsingen, kf = Konolfingen, 160 = LINIEN_TEXT
ms_kf_160 = Abbringer('160', 'Münsingen Bahnhof')

#Anschlussdefinition
an_2870a = Anschluss('Anschluss 2870 A', '31.07.2020 06:01', '00:05:00', 2, 15)

#Anschlussdefinition
an_2870b = Anschluss('Anschluss 2870 B', '31.07.2020 06:31', '00:35:00', 2, 6)

# Dummy Funktion zum testen
def anschluss_2871():
    auswertung_2871 = {(1, 2): (3, 4)}
    print(auswertung_2871)
    return auswertung_2871

# Dummy Funktion zum testen
def anschluss_2872():
    auswertung_2872 = {(5, 1): (8, 2)}
    print(auswertung_2872)
    return auswertung_2872


def anschluss_2870():
    #Daten holen
    liste_zubringer_zeiten = bn_th_s1.holezubringerzeit() # ACHTUNG feste Zuweisung! Noch anpassen!  
    liste_abbringer_zeiten = ms_kf_160.holeabbringerzeit()   # ACHTUNG feste Zuweisung! Noch anpassen!  

    #Daten auswerten    
    an_temp_tabelle = an_2870a.zubringerzeit_filtern(liste_zubringer_zeiten) # ACHTUNG feste Zuweisung! Noch anpassen! 
    auswertung_2870 = an_2870a.anschluss_suchen(an_temp_tabelle, liste_abbringer_zeiten) # ACHTUNG feste Zuweisung! Noch anpassen! 

    #Daten zurückgeben    
    print("Daten schreiben...")
    print(len(auswertung_2870))
    return auswertung_2870
