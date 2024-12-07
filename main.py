import catalogo

lista_di_dizionari = []

def main():
    print("MENU")
    print("1-stampa")
    print("Scelta")
    scelta = input(">>>")

    if(scelta == "1"):
        catalogo.dataBase(lista_di_dizionari)
        print(lista_di_dizionari)
    
if __name__ == "__main__":
    main()
