from gestioneCatalogo import inserimento, modifica, eliminazione
from statistiche import totale, genereComune, media
from raccomandazioni import analizza_generi_preferiti, genera_raccomandazioni
from catalogo import dataBase

# Catalogo iniziale
catalogo = []

def main():
    while True:
        print("\n--- Menu Principale ---")
        print("1. Gestire il catalogo")
        print("2. Visualizzare le statistiche")
        print("3. Cercare contenuti")
        print("4. Ottenere raccomandazioni personalizzate")
        print("5. Uscire dal programma")

        scelta = input("Seleziona un'opzione (1-5): ")

        if scelta == "1":
            print("\n--- Gestione Catalogo ---")
            print("a. Inserire un nuovo contenuto")
            print("b. Modificare un contenuto esistente")
            print("c. Eliminare un contenuto")
            print("d. Torna al menu principale")
            print("e. Imposta catalogo standard")
            sotto_scelta = input("Seleziona un'opzione (a-e): ")

            if sotto_scelta == "a":
                inserimento(catalogo)
            elif sotto_scelta == "b":
                modifica(catalogo)
            elif sotto_scelta == "c":
                eliminazione(catalogo)
            elif sotto_scelta == "d":
                continue
            elif sotto_scelta == "e":
                dataBase(catalogo)
            else:
                print("\nOpzione non valida. Riprova.")

        elif scelta == "2":
            print("\n--- Statistiche ---")
            film, serie = totale(catalogo)
            print(f"Numero totale di Film: {film}, Serie: {serie}")
            print("Genere più comune:")
            genereComune(catalogo)
            print("Media dei dati:")
            media(catalogo)

        elif scelta == "3":
            print("\n--- Ricerca Contenuti ---")
            criteri_validi = ["titolo", "genere", "tipo"]
            criterio = input("Cerca per (titolo/genere/tipo): ").strip().lower()

            while criterio not in criteri_validi:
                print("Input non valido. Per favore inserisci uno tra 'titolo', 'genere', 'tipo'.")
                criterio = input("Cerca per (titolo/genere/tipo): ").strip().lower()

            valore = input("Inserisci il valore da cercare: ").strip().lower()
            risultati = []

            for elemento in catalogo:
                if criterio == "titolo" and valore in elemento["titolo"].lower():
                    risultati.append(elemento)
                elif criterio == "genere" and valore in [g.lower() for g in elemento["genere"]]:
                    risultati.append(elemento)
                elif criterio == "tipo" and valore == elemento["tipo"].lower():
                    risultati.append(elemento)

            if risultati:
                print(f"\nTrovati {len(risultati)} risultati:")
                for risultato in risultati:
                    print(f"Titolo: {risultato['titolo']}, Genere: {', '.join(risultato['genere'])}, Tipo: {risultato['tipo']}")
            else:
                print("\nNessun contenuto trovato con i criteri forniti.")

        elif scelta == "4":
            print("\n--- Raccomandazioni ---")
            raccomandazioni = genera_raccomandazioni(catalogo)
            print("Raccomandazioni basate sui generi preferiti:")
            for titolo in raccomandazioni:
                print(f"- {titolo}")

        elif scelta == "5":
            print("\nGrazie per aver utilizzato il programma. Arrivederci!")
            break
        else:
            print("\nOpzione non valida. Riprova.")

if __name__ == "__main__":
    main()
