def analizza_generi_preferiti(catalogo):
    generi_preferiti = {}

    for elemento in catalogo:
        for genere in elemento["genere"]:
            if genere in generi_preferiti:
                generi_preferiti[genere] += elemento["visualizzazioni"]
            else:
                generi_preferiti[genere] = elemento["visualizzazioni"]

    generi_ordinati=sorted(generi_preferiti, key=generi_preferiti.get, reverse=True)
    
    return generi_ordinati

def genera_raccomandazioni(catalogo):
    generi_preferiti = analizza_generi_preferiti(catalogo)
    raccomandazioni = []
    titoli_aggiunti = set()

    for genere in generi_preferiti:
        for elemento in catalogo:
            if genere in elemento["genere"] and elemento["titolo"] not in titoli_aggiunti:
                raccomandazioni.append(elemento["titolo"])
                titoli_aggiunti.add(elemento["titolo"])

    raccomandazioni.sort(key=lambda titolo: next(elemento["visualizzazioni"] for elemento in catalogo if elemento["titolo"] == titolo), reverse=True)

    return raccomandazioni

