""" 
    Voimailukerhon ohjelma tulosten näyttämiseen ja laskemiseen python koodilla
    Koodin tekijä Vertti Rasi 
    Ohjelman tuottamisessa on käytetty tekoälyä
    
"""
# Alustetaan tietorakenne
tulokset = {}       # nostaja -> [(paino, tila), ...]
aktiiviset = []     # nostajat, jotka voivat vielä nostaa

def nostajan_lisaaminen(nimi):
    """
    Lisää uuden nostajan tietorakenteisiin.
    
    Parametrit:
    nimi (str): Lisättävän nostajan nimi
    """
    nimi = nimi.strip()
    if not nimi:
        print("tyhjä nimi")
        return False
    if nimi in tulokset:
        print(f"Nostaja {nimi} on jo lisätty")
        return False
    if nimi == "pois":
        return False
    
    # Luo tyhjän tuloslistan ja lisää aktiivisiin
    tulokset[nimi] = [(0, "onnistunut nosto")]
    aktiiviset.append(nimi)
    print(f"Nostaja {nimi} lisätty")
    return True

def main ():

    while True:
        nostaja = input("Nostajan nimi: ")
        nostajan_lisaaminen(nostaja)
        if nostaja == "pois":
            break
    print(tulokset)



if __name__ == "__main__":
    main()

