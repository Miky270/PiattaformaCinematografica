def totale(catalogo):
    film=0
    serie=0

    for elemento in catalogo:
        if elemento["tipo"]=="Film":
            film+=1
        else:
            serie+=1
    
    return film, serie

def genereComune(catalogo):
    generi={}

    for elemento in catalogo:
        for genere in elemento["genere"]:
            if genere in generi:
                generi[genere]+=1
            else:
                generi[genere]=1
    
    ordinati=dict(sorted(generi.items(), key=lambda item:item[1], reverse=True))

    for key,value in ordinati.items():
        print(key+": "+str(value) )
        


def media(catalogo):
    durata_tot=0
    episodi_tot=0
    film_cont=0
    serie_cont=0

    for elemento in catalogo:
        if elemento["tipo"]=="Film":
            durata_tot+=elemento["durata"]
            film_cont+=1
        elif elemento["tipo"]=="Serie":
            episodi_tot+=elemento["episodi"]
            serie_cont+=1

            
    if film_cont>0:
        durata_media=durata_tot/film_cont
    else:
        durata_media=0

    if serie_cont>0:
        episodi_media=episodi_tot/serie_cont
    else:
        episodi_media=0

    print("La durata media dei film è "+durata_media)
    print("La media del numero di episodi delle serie è "+episodi_media)