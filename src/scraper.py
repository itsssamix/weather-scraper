import time #importa biblioteca time para pausas
import logging #importa biblioteca loggings para registrar logs em arquivos
from selenium import webdriver #importa o webdriver do selenium para automação do navegador
from selenium.webdriver.common.by import By #importação para localizar elementos na página

URL = "https://weather.com/pt-BR/clima/hoje/l/BRXX0232:1:BR" #define a URL do site do clima para São Paulo, Brasil
XPATH_TEMP = "//span[@data-testid='TemperatureValue']" #localiza o elemento que contém a temperatura

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def capturar_temperatura():
    """Captura a temperatura atual no site weather.com usando Selenium."""

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled") #desativa recursos que evitam automação
        options.add_argument("--user-agent=Mozilla/5.0")

        driver = webdriver.Chrome(options=options) #Inicia o Chrome com as opções configuradas
        driver.get(URL) #abre a URL definida na constante

        time.sleep(5) #5s pra pagina carregar completamene

        temp = driver.find_element(By.XPATH, XPATH_TEMP).text
        logging.info(f"Temperatura capturada: {temp}")

        return temp

    except Exception as e:
        logging.error(f"Erro ao capturar temperatura: {e}")
        return "N/A"

    finally:
        try:
            driver.quit()
        except:
            pass