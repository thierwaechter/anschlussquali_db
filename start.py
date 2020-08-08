from datenbeschaffen import abbringer, zubringer
from datetime import datetime, timedelta

#Zubringer Angaben Anschluss 2870
linien_text_zubringer = 'S1'
zubringer_ort = 'Münsingen'
ankunft1 = '00:01:00'
ankunft2 = '00:31:00'

#Abbringer Angaben Anschluss 2870
linien_text_abbringer = '160'
abbringer_ort = 'Münsingen Bahnhof'
abfahrt1 = '00:05:00'
abfahrt2 = '00:35:00'

#Umsteigezeit Anschluss 2870
min_umsteigezeit = timedelta(minutes=2)
max_umsteigezeit1 = timedelta(minutes=6) # Für Ankunft 31
max_umsteigezeit2 = timedelta(minutes=15) # Für Ankunft 01

auswertung = {}

liste_zubringer_zeiten = zubringer(linien_text_zubringer, zubringer_ort)
liste_abbringer_zeiten = abbringer(linien_text_abbringer, abbringer_ort)


# Mit dieser neuen Zeit wird ein Anschluss beim Abbringer gesucht. Die Rückgabe ist
# "Anschluss vorhanden" oder "Kein Anschluss gefunden" inkl. der Zugeordneten Abbringerzeit.

#for an_zeit in liste_zubringer_zeiten:
#    for ab_zeit in liste_abbringer_zeiten:
#        if ab_zeit >= an_zeit + min_umsteigezeit and ab_zeit < an_zeit + max_umsteigezeit1:
#            print('Anschluss OK ' + str(an_zeit) + ' und ' + str(ab_zeit) + ' passen.')
#            break
