croissantjes = int(input('aantal croissantjes '))
prijs = 39
stokbroden = int(input('aantal stokbroden '))
bedragBrood = 278 
kortingsbonnen = int(input('aantal kortingsbonnen '))
perBon = 50 
centen = ((croissantjes * prijs) + (stokbroden * bedragBrood) - (kortingsbonnen * perBon)) / 100
factuurteks = 'de feestlunch kost bij de bakker ' + str( centen )  + ' euro voor de croissantjes en stokbroden'

print(factuurteks)

