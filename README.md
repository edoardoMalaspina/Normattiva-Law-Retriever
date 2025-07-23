# Normattiva-Law-Retriever
**Extractor of Italian law texts from Normattiva online database.**

Input some information about a law, it will find the law by sending a POST request, using ``` requests``` library, to Normattiva website. 
Once the law has been identified a headless Chrome session is started exploiting ```Selenium``` to access the full text of the law.
The full text is retrieved as html and the articles of the law are parsed using ```BeautifulSoup```bash.

## **To set up:**

Clone this repository inside your project:
```bash
git clone https://github.com/edoardoMalaspina/Normattiva-Law-Retriever.git
```

Create a virtual environment
```bash
python -m venv env_nlr
```

Activate the virtual environment:

In Windows:
```bash
.\env_nlr\Scripts\activate
```

In Ubuntu:
```bash
source env_nlr/bin/activate
```

run:
```bash
cd Normattiva-Law-Retriever
pip install -e .
cd ..
```
Now you can import in your code this package by adding:
from law_text_finder import find_law_text

## **Demo**
To test your setup simply run:
```bash
python tests/demo.py
```