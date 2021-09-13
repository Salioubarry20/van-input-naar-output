croissantjes = float(input('aantal croissantjes '))
prijs = 0.39
stokbroden = float(input('aantal stokbroden '))
bedragBrood = 2.78 
kortingsbonnen = float(input('aantal kortingsbonnen '))
perBon = 0.50 
centen = ((croissantjes * prijs) + (stokbroden * bedragBrood) - (kortingsbonnen * perBon)) * 100
factuurteks = 'de feestlunch kost bij de bakker ' + str( centen )  + ' centen voor de croissantjes en stokbroden'

print(factuurteks)

