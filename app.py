import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import tkinter as tk
from tkinter import messagebox

# Função para capturar a temperatura
def capturar_dados():
    # Configuração do Selenium (usando Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Executa em segundo plano
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=options)

    # Acessa o site de previsão do tempo
    driver.get("https://weather.com/pt-BR/clima/hoje/l/BRXX0232:1:BR")

    # Aguarda o carregamento da página
    time.sleep(5)

    try:
        # Captura a temperatura (atualize o seletor conforme necessário)
        temperatura = driver.find_element(By.XPATH, "//span[@data-testid='TemperatureValue']").text
    except:
        temperatura = "N/A"

    # Fecha o navegador
    driver.quit()

    # Retorna a temperatura capturada
    return temperatura

# Função para salvar os dados em uma planilha
def salvar_dados(temperatura):
    # Cria ou abre a planilha
    try:
        wb = Workbook()
        ws = wb.active
        ws.append(["Data/Hora", "Temperatura"])  # Apenas temperatura
    except FileNotFoundError:
        wb = Workbook()
        ws = wb.active
        ws.append(["Data/Hora", "Temperatura"])  # Apenas temperatura

    # Adiciona os dados na planilha
    data_hora = time.strftime("%Y-%m-%d %H:%M:%S")
    ws.append([data_hora, temperatura])

    # Salva a planilha
    wb.save("historico_temperatura.xlsx")

# Função para executar a captura e salvar os dados
def executar_captura():
    temperatura = capturar_dados()
    salvar_dados(temperatura)
    messagebox.showinfo("Sucesso", f"Temperatura capturada:\n{temperatura}")

# Interface gráfica
root = tk.Tk()
root.title("Captador de Temperatura de São Paulo")

btn_capturar = tk.Button(root, text="Buscar Previsão", command=executar_captura)
btn_capturar.pack(pady=20)

root.mainloop()