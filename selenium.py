from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1024,730', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


# Navegando até o site
def navegar_site(driver):
    driver.get('https://player.kovver.app/account/login/email')


# Localize os campos de entrada e insira o texto
def login(driver):
    campo_email = driver.find_element(By.ID, 'email')
    campo_senha = driver.find_element(By.ID, 'password')
    campo_email.send_keys('adrianotesteapp@gmail.com')
    campo_senha.send_keys('Testeapp@') 
    # Localize o botão de login e clique nele
    botao_login = driver.find_element(By.ID, 'email-do')
    botao_login.click()
    return print('Login efetuado')


# Localizando o web player e clicando nele
def clicando_webplayer(driver):
    link_player_web = driver.find_element(By.XPATH, '//a[contains(text(), "Player Web")]')
    link_player_web.click()
    print('Link clicado')


def clicando_no_texto(driver, texto):
    try: 
        elemento_texto = driver.find_element(By.XPATH, f'//div[contains(text(), "{texto}")]')
        elemento_texto.click()
        print(f'Click no elemento que contém {texto}')
    except:
        print()
        print(f'Elemento com texto "{texto}" não encontrado.')
        print()


def clicando_no_texto2(driver, texto):
    try:
        elemento_texto = driver.find_element(By.XPATH, f'//div[@class="item-title" and text()="{texto}"]')
        elemento_texto.click()
        print(f'Click no elemento que contém {texto}')
    except:
        print()
        print(f'Elemento com texto "{texto}" não encontrado.')
        print()


# Os códigos abaixo são para percorrer e criar uma lista dos artistas por genero musical.

# # Localizando todos os elementos com a classe "artist-thumb"
# elementos_artist_thumb = driver.find_elements(By.CSS_SELECTOR, '.artist-thumb')
# # Crie uma lista para armazenar os conteúdos do 'event_label'
# event_labels = []
# # Percorra cada elemento e obtenha o atributo 'onclick'
# for elemento in elementos_artist_thumb:
#     onclick = elemento.get_attribute('onclick')
#     # Use a função split para extrair o conteúdo do 'event_label'
#     inicio = onclick.find("'event_label' : '") + len("'event_label' : '")
#     fim = onclick.find("'", inicio)
#     event_label = onclick[inicio:fim]
#     # Adicione o conteúdo do 'event_label' à lista
#     event_labels.append(event_label)

# # Imprima os conteúdos do 'event_label'
# print(event_labels)

# # for event_label in event_labels:
# #     print(event_label)
