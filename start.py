from datenbeschaffen import abbringer, zubringer
from datetime import datetime, timedelta

#Zubringer Angaben
linien_text_zubringer = 'S1'
zubringer_ort = 'Münsingen'

#Abbringer Angaben
linien_text_abbringer = '160'
abbringer_ort = 'Münsingen Bahnhof'

#Umsteigezeit
min_umsteigezeit = timedelta(minutes=2)
max_umsteigezeit = timedelta(minutes=6)

#an_inkl_max = [] # Die Abbringerzeit inklusive der maximalen Umsteigezeit
auswertung = {}

liste_zubringer_zeiten = zubringer(linien_text_zubringer, zubringer_ort)
print(liste_zubringer_zeiten)
liste_abbringer_zeiten = abbringer(linien_text_abbringer, abbringer_ort)
print(liste_abbringer_zeiten)

# Zur Zubringerzeit wird die maximale Umseigezeit gerechnet. Dank der Umwandlung funtioniert die 
# Rechnung auch um Mittarnacht
#for zeit_str in liste_zubringer_zeiten:
#    zeit = datetime.strptime(zeit_str, "%d.%m.%Y %H:%M:%S")
#    max_zeit = zeit + max_umsteigezeit
#    an_inkl_max.append(max_zeit)

# Mit dieser neuen Zeit wird ein Anschluss beim Abbringer gesucht. Die Rückgabe ist
# "Anschluss vorhanden" oder "Kein Anschluss gefunden" inkl. der Zugeordneten Abbringerzeit.

for an_zeit in liste_zubringer_zeiten:
    for ab_zeit in liste_abbringer_zeiten:
        if ab_zeit > an_zeit + min_umsteigezeit and ab_zeit < an_zeit + max_umsteigezeit:
            print('Anschluss OK ' + str(an_zeit) + ' und ' + str(ab_zeit) + ' passen.')
            break
