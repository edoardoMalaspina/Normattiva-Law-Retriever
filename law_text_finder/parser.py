from bs4 import BeautifulSoup


# Exploit BeautifulSoup to extract the relevant text of a law
# from the html of the full text page
def parse_law_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    # Find the tag of the articles of the law
    body_divs = soup.find_all("div", class_="bodyTesto")

    # if at least one article found
    if body_divs:
        # Concatenate all the articles into a single text
        full_text = ""
        for idx, div in enumerate(body_divs, start=1):
            testo = div.get_text(separator="\n", strip=True)
            full_text = full_text,  testo


    return full_text
    

    
