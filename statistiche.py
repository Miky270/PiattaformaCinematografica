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
    
    for key in dict(sorted(generi.items(), key= lambda item:item[1], reverse=True)):
        pass
        

def media():
    pass