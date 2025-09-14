# Cortes Fregoso Karla Stephanie (2209422) Grupo951
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def extraer(html: str, datos: dict):
    soup = BeautifulSoup(html, "html.parser")
    productos = soup.find_all("div", {"data-component-type": "s-search-result"})

    for p in productos:
        titulo, precio, rating, entrega = "N/D", "N/D", "N/D", "N/D"

        #Titulo
        t = p.select_one("h2 a span")
        if t:
            titulo = t.get_text(strip=True)

        #Precio
        pr = p.select_one("span.a-offscreen")
        if pr:
            precio = pr.get_text(strip=True)

        #Rating
        r = p.select_one("span.a-icon-alt")
        if r:
            rating = r.get_text(strip=True)

        try:
            entrega_el = p.find_element(By.CSS_SELECTOR, "span.a-color-base.a-text-bold, span.a-color-secondary")
            entrega = entrega_el.text.strip()
        except:
            entrega = "N/D"

        datos["titulo"].append(titulo)
        datos["precio"].append(precio)
        datos["rating"].append(rating)
        datos["entrega"].append(entrega)



def navegacion(producto: str, paginas: int = 1):
    #Configurar navegador
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1200x1000")
    navegador = webdriver.Chrome(service=s, options=opc)

    #Diccionario
    datos = {"titulo": [], "precio": [], "rating": [], "entrega": []}

    try:
        navegador.get("https://www.amazon.com.mx/")
        time.sleep(2)

        buscador = navegador.find_element(By.ID, "twotabsearchtextbox")
        buscador.send_keys(producto)
        navegador.find_element(By.ID, "nav-search-submit-button").click()
        time.sleep(3)

        for i in range(paginas):
            extraer(navegador.page_source, datos)

            #Pasar a la siguiente pagina
            try:
                next_btn = navegador.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
                if next_btn.get_attribute("aria-disabled") == "true":
                    break
                next_btn.click()
                time.sleep(3)
            except:
                break

    finally:
        navegador.close()

    #Crear DataFrame y CSV
    df = pd.DataFrame(datos)
    df.to_csv(f"dataset/Amazon.csv")


if __name__ == "__main__":
    navegacion("Labial", 2)
