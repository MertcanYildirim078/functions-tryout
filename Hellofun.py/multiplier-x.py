tafel = int(input('Welke tafel wil je zien? '))

def tafels(tafel):
    for x in range(1,11):
        totaal = x * tafel
        print (totaal)
        

tafels(tafel)
