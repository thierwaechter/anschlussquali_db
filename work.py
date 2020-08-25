from datetime import datetime, timedelta
import csv

class Master():
    def __init__(self):
        self.__master_output = {} 

    def master_beschreiben(self, temp_dic):
        self.__master_output.update(temp_dic) 

    def master_lesen(self):
        return self.__master_output


class FilterZubringerAbbringer():
    def __init__(self, linien_text, haltestellen_name):
        self.linien_text = linien_text
        self.haltestellen_name = haltestellen_name
        self.zubringer_zeiten = []
        self.abbringer_zeiten = []

    def holezubringerzeit(self):
        print("Daten Zubringer werden gesucht...")
        with open('2020-07-31_istdaten.csv', newline='') as file:
            linereader = csv.reader(file, delimiter=';', quotechar='"')
            for line in linereader:
                if line[7] == self.linien_text and line[13] == self.haltestellen_name:
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
                    self.zubringer_zeiten.append(zubringer_tupel)

            print(len(self.zubringer_zeiten))        
            return self.zubringer_zeiten

    def holeabbringerzeit(self):
        print("Daten Abbringer werden gesucht...")
        with open('2020-07-31_istdaten.csv', newline='') as file:
            linereader = csv.reader(file, delimiter=';', quotechar='"')
            for line in linereader:
                if line[7] == self.linien_text and line[13] ==  self.haltestellen_name:
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
                    self.abbringer_zeiten.append(abbringer_tupel)
            print(len(self.abbringer_zeiten))
            return self.abbringer_zeiten

class FilterZubringerAnkunft():
    def __init__(self, name, ankunft_str, abfahrt_str, min_umsteigezeit_int, max_umsteigezeit_int, anzahl):
        self.name = name
        self.ankunft_str = ankunft_str
        self.abfahrt_str = abfahrt_str
        self.min_umsteigezeit_int = min_umsteigezeit_int
        self.max_umsteigezeit_int = max_umsteigezeit_int
        self.anzahl = anzahl
        self.anschluesse_dic = {}
        self.min_umsteigezeit = timedelta(minutes=self.min_umsteigezeit_int)
        self.max_umsteigezeit = timedelta(minutes=self.max_umsteigezeit_int)
        self.ankunft = datetime.strptime(self.ankunft_str, '%d.%m.%Y %H:%M')


    def filtern_suchen(self, liste_zubringer_zeiten, liste_abbringer_zeiten):
        print('Zubringer aus Haupttabelle filtern und passende Anschlüsse suchen...')
        an_temp_tabelle = []
        for i in range(self.anzahl): 
            for ankunftszeit in liste_zubringer_zeiten:
                if  ankunftszeit[0] == self.ankunft:
                    an_temp_tabelle.append(ankunftszeit)
            self.ankunft = self.ankunft + timedelta(hours=1)
        print(len(an_temp_tabelle))
        for an_zeit in an_temp_tabelle:
            for ab_zeit in liste_abbringer_zeiten:
                if ab_zeit[1] >= an_zeit[1] + self.min_umsteigezeit and ab_zeit[1] <= an_zeit[1] + self.max_umsteigezeit:
                    self.anschluesse_dic[an_zeit] = ab_zeit
                    break      
                else: 
                    self.anschluesse_dic[an_zeit] = (0, 0)      
        return self.anschluesse_dic

class FilterAbbringerAbfahrt():
    def __init__(self, anschluss_name, zubringer_name, abbringer_name, zubringer, abbringer, anschlussdefinition):
        self.anschluss_name = anschluss_name
        self.zubrninger_name = zubringer_name
        self.abbringer_name = abbringer_name
        self.zubringer = zubringer
        self.abbringer = abbringer
        self.anschlussdefinition = anschlussdefinition
        self.total_gefundene_anschluesse_dic = {}

    def __len__(self):
        return len(self.total_gefundene_anschluesse_dic) 

    def anschluesse_schreiben(self):
        liste_zubringer_zeiten = self.zubringer.holezubringerzeit()
        liste_abbringer_zeiten = self.abbringer.holeabbringerzeit()

        for item in self.anschlussdefinition:
            temp_auswertung = item.filtern_suchen(liste_zubringer_zeiten, liste_abbringer_zeiten)
            self.total_gefundene_anschluesse_dic.update(temp_auswertung)

        temp_dic = {}
        print("Reichere Daten an...")
        for key in self.total_gefundene_anschluesse_dic:
            temp_dic[(self.zubrninger_name,) + key] = self.total_gefundene_anschluesse_dic[key]
        for key, value in temp_dic.items():
            temp_dic[key] = (self.abbringer_name,) + value
     
        print("Daten werden in Mastertabelle geschrieben...")
        temp_dic[self.anschluss_name] = temp_dic
        self.master_beschreiben(temp_dic)


#    def anschluesse_auswerten(self):
#        gehalten = {}
#        nicht_gehalten = {}
#        for key, value in self.total_gefundene_anschluesse_dic:
#            if value == 0:
#                nicht_gehalten[key] = value
#            else:
#                gehalten[key] = value
#
#        ergebnis_auswertung = [len(gehalten), len(nicht_gehalten)]
#        return ergebnis_auswertung
#
#    def anschluesse_mastertabelle(self, total_gefundene_anschluesse_dic):
#        master_output = {}
#        master_output.update({self.name})
#        print("Master Output: " + master_output)
#        for key in self.total_gefundene_anschluesse_dic:

class Anschlussdaten():
    def __init__(self, anschlussnummer):
        self.anschlussnummer = anschlussnummer

    def anschluss(self):
        with open('Basisdaten_Anschluesse.csv', newline='') as file:
            linereader = csv.reader(file, delimiter=';', quotechar='"')
            for line in linereader:
                if line[0] == self.anschlussnummer:
                    line[1] = FilterZubringerAbbringer(line[2], line[3])
                    line[4] = FilterZubringerAbbringer(line[5], line[6])
                    line[7] = FilterZubringerAnkunft()




def anschluss_2870():

    #bn = Bern, th = Thun, s1 = LINIEN_TEXT
    #ms = Münsingen, kf = Konolfingen, 160 = LINIEN_TEXT
    #Achtung: Bei den Anschlüssen muss die Startzeit angegeben werden. Danach werden 
    #Anschlüsse so oft wie die letzte Zahl lautet, gesucht.
    
    bn_th_s1 = FilterZubringerAbbringer('S1', 'Münsingen')
    ms_kf_160 = FilterZubringerAbbringer('160', 'Münsingen Bahnhof')
    an_2870a = FilterZubringerAnkunft('Anschluss 2870 A', '31.07.2020 06:01', '00:05:00', 2, 15, 15)
    an_2870b = FilterZubringerAnkunft('Anschluss 2870 B', '31.07.2020 06:31', '00:35:00', 2, 6, 14)

    anschluss2870 = FilterAbbringerAbfahrt("2870", 'bn_th_s1', 'ms_kf_160', bn_th_s1, ms_kf_160, [an_2870a, an_2870b])
    anschluss2870.anschluesse_schreiben()
    #auswertung_anschluss2870 = anschluss2870.anschluesse_auswerten()



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

def anschluss_1260():

    #ost = Ostermundigen, rub = Rubigen, s2 = LINIEN_TEXT
    #fm = Fischemätteli, wb = Worb Dorf, 6 = LINIEN_TEXT
    #Achtung: Bei den Anschlüssen muss die Startzeit angegeben werden. Danach werden 
    #Anschlüsse so oft wie die letzte Zahl lautet, gesucht.
    
    ost_rub_s2 = FilterZubringerAbbringer('S2', 'Gümligen')
    fm_wb_6 = FilterZubringerAbbringer('6', 'Gümligen Bahnhof')
    an_1260a = FilterZubringerAnkunft('Anschluss 1260', '31.07.2020 21:21', '00:25:30', 2, 5, 15)
    an_1260b = FilterZubringerAnkunft('Anschluss 1260', '31.07.2020 21:51', '00:25:30', 2, 5, 15)


    anschluss1260 = FilterAbbringerAbfahrt("1260", 'ost_rub_s2', 'fm_wb_6', ost_rub_s2, fm_wb_6, [an_1260a, an_1260b])
    anschluss1260.anschluesse_schreiben()
