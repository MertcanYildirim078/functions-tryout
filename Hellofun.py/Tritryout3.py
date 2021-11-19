def persoon( ):
    OGnaam = 'niks'
    leeftijd = 'niks'
    vragen = True
    while vragen:
        naam = input('Geef uw naam: (zeg stop als u wilt stoppen)')
        if naam == 'stop':
            break
        OGnaam = naam
        leeftijd = int (input('Geef uw leeftijd jaar: '))

    return OGnaam, leeftijd

name,age = persoon()

print(f'De naam is {name}. De leeftijd is {age}')

