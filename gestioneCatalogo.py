from datetime import datetime

def inserimento(catalogo):
    titolo = input("Inserisci il titolo: ")
    genere = set(input("Inserisci i generi separati da virgola: ").split(','))
    tipo = input("Inserisci il tipo (Film o Serie): ")
    durata = int(input("Inserisci la durata in minuti: "))
    episodi = int(input("Inserisci il numero di episodi: "))
    visualizzazioni = int(input("Inserisci il numero di visualizzazioni: "))

    nuovo_contenuto = {
        "titolo": titolo,
        "genere": genere,
        "tipo": tipo,
        "durata": durata,
        "episodi": episodi,
        "data_inserimento": datetime.now(),
        "data_modifica": datetime.now(),
        "visualizzazioni": visualizzazioni
    }
    catalogo.append(nuovo_contenuto)

def modifica(catalogo):
    titolo = input("Inserisci il titolo del contenuto da modificare: ")
    for elemento in catalogo:
        if elemento["titolo"] == titolo:
            print("Lascia vuoto un campo per non modificarlo.")
            nuovo_titolo = input(f"Nuovo titolo ({elemento['titolo']}): ") or elemento["titolo"]
            nuovo_genere = input(f"Nuovi generi ({','.join(elemento['genere'])}): ")                #non posso usare or perché lo split mi returna comunque qualcosa che viene contato come True e quindi viene scelto
            nuovo_genere = set(nuovo_genere.split(',')) if nuovo_genere else elemento["genere"]
            nuovo_tipo = input(f"Nuovo tipo ({elemento['tipo']}): ") or elemento["tipo"]
            nuova_durata = int(input(f"Nuova durata ({elemento['durata']}): ") or elemento["durata"])
            nuovi_episodi = int(input(f"Nuovi episodi ({elemento['episodi']}): ") or elemento["episodi"])
            nuove_visualizzazioni = input(f"Nuove visualizzazioni ({elemento['visualizzazioni']}): ") or elemento["visualizzazioni"]

            elemento.update({
                "titolo": nuovo_titolo,
                "genere": nuovo_genere,
                "tipo": nuovo_tipo,
                "durata": nuova_durata,
                "episodi": nuovi_episodi,
                "visualizzazioni": nuove_visualizzazioni,
                "data_modifica": datetime.now()
            })
            return
    print(f"Contenuto con titolo '{titolo}' non trovato nel catalogo.")

def eliminazione(catalogo):
    titolo = input("Inserisci il titolo del contenuto da eliminare: ")
    for i, elemento in enumerate(catalogo):             #i é l'indice della lista ed elemento é il dizionario
        if elemento["titolo"] == titolo:
            del catalogo[i]
            print(f"Contenuto con titolo '{titolo}' eliminato dal catalogo.")
            return
    print(f"Contenuto con titolo '{titolo}' non trovato nel catalogo.")
