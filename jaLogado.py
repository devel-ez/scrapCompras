import time

from funcoes import *

# Acessar a página de contratos
driver.get("https://contratos.comprasnet.gov.br/gescon/contrato?situacao=[1]")
# Esperar alguns segundos para que a página seja carregada
driver.implicitly_wait(10)  # Aguarde até 10 segundos para elementos carregarem, se necessário

clicarVisibilidadeColuna()
clicarRegistroPorPagina()
time.sleep(3)
clicarCopiar()

# Acessar a planilha do google sheets
driver.get("https://docs.google.com/spreadsheets/d/1Kk-PjMIrY1Qa3jF_Bdco9fVb_PUhykEPRUz-juME5ls/edit?pli=1#gid=0")
# Esperar alguns segundos para que a página seja carregada
driver.implicitly_wait(10)  # Aguarde até 10 segundos para elementos carregarem, se necessário

colarNaPlanilhaContratos()

# Adicionar uma pausa para que você possa ver o resultado após o clique
input("Pressione Enter para fechar o navegador...")

# Fechar o navegador
driver.quit()