toegangsticket = 7.45
vr_gameseat = 0.37


aantal_personen = int(input("Met hoeveel ben je?: "))
aantal_minuten_gameseat = int(input("Hoeveel minuten wil je in de VR-Gameseat?: "))
totaalkosten_tickets = float(toegangsticket * aantal_personen)
totaalkosten_VR = float(aantal_minuten_gameseat * vr_gameseat * aantal_personen)
Totaal_Alles = float(totaalkosten_tickets + totaalkosten_VR)


print('Het kost: €' + str(Totaal_Alles))



