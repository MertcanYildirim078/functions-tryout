def Play(place):
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('WELKOM BIJ DE SUBNAUTICA GAME!')
    print('BIJ DEZE GAME GA JE DOOR EEN AVONTUUR ONDERWATER, DAT NIET VEILIG IS...') #Mertcan Yildirim 99068314
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Je bent op een onbekende wereld die 4546B heet. Je bent midden het oceaan in je Lifepod(je bovenwater huisje).')
    print('Je hebt een Scuba outfit dus kun je gewoon onderwater zwemmen.')
    print('Je was in een grote ruimte schip die op deze wereld stortte.')
    print('Je moet een keuze maken waar je naartoe wilt gaan voor je avontuur.')
    print('Je moet ook spullen vinden om te overleven dus wees wijs over je keuzes!')
    print('Waarschuwing: Geen spullen/eten en niet terug = verlies!')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    place = input('crashsite of eiland? ')
    if place == '':
        print('Dood gegaan van de honger!')                        #(Crash site of Richting een eiland in de verte)
    if place == 'crashsite':
        Crashsite2 = input('Tijdens het reizen naar de crashsite zie je in de verte een Reaper Leviathan(grote haai). Proberen verslaan met een mes voor eten of ontwijken? v/o ')
        if Crashsite2 == 'v':
            print('Toen je al probeerde vlakbijer te komen at hij jou op. Verlies!')
        else:
            Crashsite3 = input('Je bent net levend uitgekomen door de leviathan te ontwijken en heb je wat HP verloren.' + '\n'
            'Je ziet een gevallen kist liggen op de bodem vlakbij de Crashsite. Pakken of verder gaan? p/v ')
            if Crashsite3 == 'p':
                print ('Je hebt de kist snel kunnen pakken en je hebt een medkit, water en eten gevonden in de kist en gebruikte de medkit voor 50% HP.' + '\n'
                'Nu nog terug te gaan naar je Lifepod en had je teveel zelf vertouwen om langs de Reaper leviathan te gaan en had je geen geluk om te ontywijken. Verlies!')
            else:
                print('Je bent bij de Crashsite en vond een entree om in de schip te kunnen komen. Er zou nog veel spullen binnen liggen maar er is brand.' + '\n'
                'Je gaat naar binnen en probeert de vuur te ontwijken. Na een tijd dat je voorzichtig langs de vuur ging had je weinig HP.' + '\n'
                'Je kwam bij een kamer met eten en drinken, maar je zag bij de overstaande kamer een communicatie computer om hulp te vragen.' + '\n'
                'Je ging ernaar toe en vroeg om hulp en kwam er net heel uit en naar je Seapod. Win!')
    elif place == 'eiland':
        Eiland = input('Je ziet een eiland in de verte, gaan of niet? g/n ')
        if Eiland == 'g':
            Eiland2 = input('Het was een lange reis en kwam bij het lange eiland maar je had erg dorst en honger. Er was op de eiland veel tropiale bomen met vruchten voor water en eten.' + '\n'
            'Je ging het opeten en bracht wat mee naar je Lifepod. Onderweg kwam je een Sandshark je aanvallen dus moest je een snelle keuze om in een onderwater cave te gaan snel of verder zwemmen. Cave of snel verder? c/s ')
            if Eiland2 == 'c':
                print('Je was bij de cave en was ontsnapt van Sandshark. Het was donker en zag je verschillende vissen zwemmen die gevaarlijk lijken.' + '\n'
                'Je besloot weer uit de cave te gaan en naar je Lifepod te gaan en kwam de Sandshark verstopt in zand en at je op. Verlies!')
            else:
                Eiland3 = input('Je bent spoedig naar het Lifepod gezwommen terwijl de Sandshark je zat te achtervolgen en heeft het overleeft.' + '\n'
                'Maar je raakte de weg kwijt doordat je in paniek raakte en ging het steeds dieper als je ging. Tegenovergestelde richting gaan of niet? g/n ')
                if Eiland3 == 'n':
                    print('Je ging terug maar de Sandshark zag je die je ontsnapt had maar was je moe geraakt toen je probeerde te ontsnappen en at hij je op. Verlies!')
                else:
                    Eiland4 = input('Je ging steeds dieper en kwam je op 400 meter diepte. Er waren wat gevaarlijke vissen waardoor je voorzichtig langs ging.' + '\n'
                    'Je zag in de verte wat licht dat leek op een onderwater fort, je ging ernaar toe en er waren mensen die je ko helpen. In de fort gaan of niet? g/n ')
                    if Eiland4 == 'n':
                        print('Dood gegaan door geen oxygen!')
                    else:
                        Eiland5 = input('Je ging via een klep naar binnen en er waren watervoertuigen en was het best groot. Je zag niemand in de buurt en ging stiekem snel naar een kamer voor je en zag je buit' + '\n'
                        'Je kunt de buit pakken en ontsnappen. Pakken of niet? p/n ')
                        if Eiland5 == 'p':
                            print('Tijdens het ontsnappen kwam je toevallig iemand tegen. Hij zag je met je loot en schoot hij je neer, verlies!')
                        else:
                            Eiland6 = input('Je ging uit de kamer met de buit en kwam je iemand tegen die vroeg om wie je was, je vertelde alles over de situatie en begreep dat je hulp nodig had.' + '\n'
                            'Hij zij dat je hier mocht blijven en dat hij alleen woonde, hij gaf je voedsel en spullen. Er was van alles in de fort zoals een machine dat water maakt en medicijnen.' + '\n'
                            'Je had de mogelijkheid om hem te vermoorden met je mes, vermoorden of niet? v/n ')
                            if Eiland6 == 'v':
                                print('Het is je gelukt om hem te vermoorden en was de hele fort van jou. Kwaadaardige Win!')
                            else:
                                print('Jullie zijn gelukkig samen in de fort aan het overleven en elkaar helpen. Gelukkige Win!')  
Play(place = '')                                
 #Je kunt hier ook de place veranderen door eiland of crashsite door de return

