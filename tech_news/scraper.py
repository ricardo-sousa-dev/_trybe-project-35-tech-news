import requests  # importa o módulo requests para fazer a requisição HTTP
import time  # importa o módulo time para simular um delay
import parsel  # importa o módulo parsel para fazer o parsing do HTML

url_da_noticia = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url, timeout=3):
    """Faz uma requisição HTTP e retorna o conteúdo HTML"""
    time.sleep(1)  # Simula um delay de 1 segundo
    try:
        response = requests.get(url, timeout=timeout)  # Faz a requisição HTTP
        response.raise_for_status()  # Se a requisição falhou, lança um erro
    except (requests.HTTPError, requests.ReadTimeout):  # captura o erro
        return None

    return response.text  # retorna o conteúdo HTML


html_content = fetch(url_da_noticia)
# print(html_content)


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
