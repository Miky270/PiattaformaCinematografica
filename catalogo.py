from datetime import datetime, timedelta

def dataBase(lista_di_dizionari):
    new = [
        {
            "titolo": "Matrix",
            "genere": {"Fantascienza"},
            "tipo": "Film",
            "durata": 136,
            "episodi": None,
            "data_inserimento": datetime(2024, 1, 15),
            "data_modifica": datetime(2024, 1, 15),
            "visualizzazioni": 5
        },
        
        {
            "titolo": "Inception",
            "genere": {"Fantascienza"},
            "tipo": "Film",
            "durata": 148,
            "episodi": None,
            "data_inserimento": datetime(2024, 1, 20),
            "data_modifica": datetime(2024, 1, 20),
            "visualizzazioni": 3
        },
        
        {
            "titolo": "The Witcher",
            "genere": {"Fantasy"},
            "tipo": "Serie",
            "durata": None,
            "episodi": 8,
            "data_inserimento": datetime(2024, 2, 1),
            "data_modifica": datetime(2024, 2, 1),
            "visualizzazioni": 12
        },
        
        {
            "titolo": "Il Signore degli Anelli",
            "genere": {"Fantasy"},
            "tipo": "Film",
            "durata": 201,
            "episodi": None,
            "data_inserimento": datetime(2024, 3, 5),
            "data_modifica": datetime(2024, 3, 5),
            "visualizzazioni": 8
        },
        
        {
            "titolo": "Stranger Things",
            "genere": {"Fantascienza", "Horror"},
            "tipo": "Serie",
            "durata": None,
            "episodi": 8,
            "data_inserimento": datetime(2024, 2, 15),
            "data_modifica": datetime(2024, 2, 15),
            "visualizzazioni": 6
        }
    ]
    
    lista_di_dizionari.extend(new)
