import urllib.parse

from src.fake_browser import click_full_article_link
from src.parser import parse_law_text_from_html
from src.request import retrieve_law_page


# Method to find the text of a law
# input: denomination: kind of law requested (COSTITUZIONE/DECRETO/LEGGE/DELIBERAZIONE)
#        text: text to put in the search bar
#        start_date: starting date for the research
#        end_date: end date for the research
def find_law_text(denomination, text, start_date, end_date):

    # Retrieve the list of laws from the research
    data = retrieve_law_page(denomination, 
                         text,
                         start_date,
                         end_date)

    if data["numeroAttiTrovati"] == 0:
        print("Nessun atto trovato.")
        exit()

    # Extract the best result from the list
    atto = data["listaAtti"][0]

    # Retrieve informations from the extracted law
    codice = atto["codiceRedazionale"]
    data_gu = atto["dataGU"]

    # Compose the URL for the extracted law
    params = {
        "atto.dataPubblicazioneGazzetta": data_gu,
        "atto.codiceRedazionale": codice,
        "atto.articolo.numero": 0,
        "atto.articolo.sottoArticolo": 1,
        "atto.articolo.sottoArticolo1": 0,
        "qId": "",
        "tabID": "0.0",
        "title": "lbl.dettaglioAtto"
    }
    url_full_article = "https://www.normattiva.it/atto/caricaDettaglioAtto?" + urllib.parse.urlencode(params)
    
    # Start a fake chrome session to click on the link
    # to show the full text of the article
    html_page = click_full_article_link(url_full_article)

    # Parse the full text of the article from html
    law_text = parse_law_text_from_html(html_page)

    return law_text

