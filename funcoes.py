import requests
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyautogui

# Criar um objeto Options e definir o perfil personalizado
chrome_options = Options()
chrome_options.add_argument('--user-data-dir={}'.format('C:\\Users\\Felipe\\PycharmProjects\\ContratosCompras\\seleniumPerfilChromeDriver'))

# Inicializar o driver do Chrome
driver = uc.Chrome(executable_path="C:\\Users\\Felipe\\PycharmProjects\\ContratosCompras\\chromedriver-win64", options=chrome_options)


def clicarVisibilidadeColuna():
    # Localizar o botão VISIBILIDADE DA COLUNA e selecionar as colunas que deverão ficar visiveis
    try:
        botao_visibilidadeColuna = driver.find_element(By.XPATH, '//*[@id="datatable_button_stack"]/div/button[1]')
        botao_visibilidadeColuna.click()
        botao_requisitantes = driver.find_element(By.XPATH, '//*[@id="datatable_button_stack"]/div/ul/li[5]/a')
        botao_requisitantes.click()
        botao_objeto = driver.find_element(By.XPATH, '//*[@id="datatable_button_stack"]/div/ul/li[12]/a')
        botao_objeto.click()
        botao_numParcelas = driver.find_element(By.XPATH, '//*[@id="datatable_button_stack"]/div/ul/li[17]/a')
        botao_numParcelas.click()
        botao_valorParcelas = driver.find_element(By.XPATH, '//*[@id="datatable_button_stack"]/div/ul/li[18]/a')
        botao_valorParcelas.click()
        botao_atualizado = driver.find_element(By.XPATH, '//*[@id="datatable_button_stack"]/div/ul/li[24]/a')
        botao_atualizado.click()

        print('Botão "visibilidadeColuna" clicado com sucesso!')
    except Exception as e:
        print(f'Erro ao clicar no botão "visibilidadeColuna": {e}')

    # Esperar alguns segundos para que a página seja carregada
    driver.implicitly_wait(10)  # Aguarde até 10 segundos para elementos carregarem, se necessário

def clicarRegistroPorPagina():
    # Localizar o botão registros por páginas e selecionar TODOS
    try:
        botao_registrosPorPagina = driver.find_element(By.XPATH, '//*[@id="crudTable_length"]/label/select/option[5]')
        botao_registrosPorPagina.click()


        print('Botão "registrosPorPagina" clicado com sucesso!')
    except Exception as e:
        print(f'Erro ao clicar no botão "registrosPorPagina": {e}')

    # Esperar alguns segundos para que a página seja carregada
    driver.implicitly_wait(10)  # Aguarde até 10 segundos para elementos carregarem, se necessário

def clicarCopiar():
    # Localizar o botão copiar
    try:
        botao_copiar = driver.find_element(By.XPATH, '//*[@id="datatable_button_stack"]/div/button[2]/span')
        botao_copiar.click()


        print('Botão "copiar" clicado com sucesso!')
    except Exception as e:
        print(f'Erro ao clicar no botão "copiar": {e}')

    # Esperar alguns segundos para que a página seja carregada
    driver.implicitly_wait(10)  # Aguarde até 10 segundos para elementos carregarem, se necessário

def colarNaPlanilhaContratos():
    # colar na planilha
    try:
        time.sleep(3)
        pyautogui.press('esc')
        pyautogui.hotkey('ctrl', 'v')

        print('Colado na planilha com sucesso!')
    except Exception as e:
        print(f'Erro ao colar na planilha": {e}')

    # Esperar alguns segundos para que a página seja carregada
    driver.implicitly_wait(10)  # Aguarde até 10 segundos para elementos carregarem, se necessário