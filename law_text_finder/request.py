import requests


def retrieve_law_page(denominazione_atto, testo_ricerca, data_inizio_emanazione, data_fine_emanazione):
    URL = "https://api.normattiva.it/t/normattiva.api/bff-opendata/v1/api/v1/ricerca/avanzata"

    payload = {
        "denominazioneAtto": f"{denominazione_atto}",
        "titoloRicerca":"legge",
        "testoRicerca": f"{testo_ricerca}",
        "dataInizioEmanazione": f"{data_inizio_emanazione}",
        "dataFineEmanazione": f"{data_fine_emanazione}",
        "paginazione": {
            "paginaCorrente": 0,
            "numeroElementiPerPagina": 10
        },
        "limitaAnniVigenza": False,
        "filtriMap": {}
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "python-requests"
    }

    response = requests.post(URL, json=payload, headers=headers)
    
    data = response.json()

    return data