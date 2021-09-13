toegangsticket = 7.45
personen = float(input('personen ')) 
aantalGameseatMinuten = 45
kostenPerMinuten = float(input('kosten per minute ')) 
prijsPerMinuten = 45
personenVrienden = float(input('prijs per minuten ')) 
centen = (toegangsticket) * (personen) + (aantalGameseatMinuten) / (kostenPerMinuten) + (prijsPerMinuten) * (personenVrienden) * 100
factuurteks = 'de kosten in totaal zijn ' + str(centen) + ' centen'

print(factuurteks)
