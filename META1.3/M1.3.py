# Cortes Fregoso Karla Stephanie (2209422) Grupo951

#Librerias
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def navegacion(producto,paginas):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020x1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com.mx/")
    time.sleep(2)

    #Buscar producto
    buscador = navegador.find_element(By.ID, "twotabsearchtextbox")
    buscador.clear()
    buscador.send_keys(producto)

    boton = navegador.find_element(By.ID, "nav-search-submit-button")
    boton.click()
    time.sleep(3)

    base = producto.replace(" ", "_").lower()
    for pag in range(paginas):
        #Guardar captura
        navegador.save_screenshot(f"imagenes/amazon_{base}_p{pag}.png")
        time.sleep(1)

        #Ir a la siguiente pagina
        try:
            next_btn = navegador.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
            if next_btn.get_attribute("aria-disabled") == "true":
                break
            next_btn.click()
            time.sleep(3)
        except:
            break

    navegador.close()


if __name__ == "__main__":
    navegacion("Labial",2)