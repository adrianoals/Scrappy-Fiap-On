from selenium_func import *
from time import sleep
from vimeo_downloader import Vimeo
import re
from dotenv import load_dotenv
from pathlib import os

load_dotenv()

site = 'https://www2.fiap.com.br/'

driver = iniciar_driver()

navegar_site(driver, site)

# Aguardando até que o elemento esteja presente
sleep(5)

# Preenchendo RM
campo_rm = driver.find_element(By.ID, 'usuario')
campo_rm.send_keys(os.getenv('RM'))
# Preenchendo senha
campo_senha = driver.find_element(By.ID, 'senha')
campo_senha.send_keys(os.getenv('SENHA'))
# Clicando em conectar
botao_conectar = driver.find_element(By.CLASS_NAME, 'a-login-btn')
botao_conectar.click()

# Adicionando pausa
sleep(5)

# Navegando até o capítulo
url = 'https://on.fiap.com.br/local/salavirtual/conteudo-video.php?c=9053&id=318420'

navegar_site(driver, url)

data_name_list = []
data_link_list = []

sleep(5)


elements = driver.find_elements(By.CSS_SELECTOR, 'div.conteudo-video-list-item.js-video-play')

for element in elements:
    data_name = element.get_attribute('data-name')
    data_link = element.get_attribute('data-link')
    
    data_name_list.append(data_name)
    data_link_list.append(data_link)

print(data_name_list)
print(data_link_list)
print()


for link_video, nome_video, in zip(data_link_list, data_name_list):
    # Crie uma instância do Vimeo com a URL do vídeo e a URL onde ele está incorporado
    link_videos = Vimeo(link_video, embedded_on=url)
    # Obtenha os streams disponíveis para o vídeo
    quality_video = link_videos.streams
    print(quality_video)

    # Selecione o melhor stream (geralmente o último na lista)
    best_stream = quality_video[-1]

    # Remova caracteres inválidos do nome do arquivo
    nome_video = re.sub(r'[\\/*?:"<>|]', "", nome_video)

    # Baixe o vídeo
    best_stream.download(download_directory='DirectoryName', filename=nome_video)



# antes de fehar a automacao
input('digite algo para fechar... ')