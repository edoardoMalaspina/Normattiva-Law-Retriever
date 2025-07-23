from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Use Selenium to start a headless Google Chrome session
# to click the link to the full text of the law
# (necessary to avoid problems related to JS code in the scraped page)
def click_full_article_link(page_url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    try:
        # Give time to load the JavaScript (max 10 seconds)
        wait = WebDriverWait(driver, 10)

        # Open the page
        driver.get(page_url)

        # Find the link to the full text
        export_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href^="/esporta/attoCompleto"]'))
        )
        href = export_link.get_attribute("href")

        # Follow the link
        driver.get(href)

        # === Step 7: Estrai div con bodyTesto ===
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.bodyTesto"))
        )

        # Get the source of the full text page 
        html_page = driver.page_source
        
    finally:
        driver.quit()

    return html_page
