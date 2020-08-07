from datenbeschaffen import abbringer, zubringer

#Zubringer Angaben
linien_text_zubringer = 'S1'
zubringer_ort = 'Münsingen'

#Abbringer Angaben
linien_text_abbringer = '160'
abbringer_ort = 'Münsingen Bahnhof'

#Umsteigezeit
max_umsteigezeit: 360 #in Sekunden

auswertung = {}

#liste_zubringer_zeiten = zubringer(linien_text_zubringer, zubringer_ort)
liste_abbringer_zeiten = abbringer(linien_text_abbringer, abbringer_ort)
#print(liste_zubringer_zeiten)
print(liste_abbringer_zeiten)