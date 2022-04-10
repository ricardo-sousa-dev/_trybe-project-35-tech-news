import requests  # importa o módulo requests para fazer a requisição HTTP
import time  # importa o módulo time para simular um delay
from parsel import Selector  # importa o módulo parsel para fazer parse do HTML


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


html_content = fetch(url_da_noticia)  # Armazena o html da page
# print(html_content)


# Requisito 2
def scrape_novidades(html_content):
    # Parseia o HTML
    page = Selector(html_content)
    list_news = []
    # for pega todos os artigos da página
    for article in page.css("div.tec--list__item"):
        # pega a url do artigo
        url_notice = article.css("a.tec--card__title__link::attr(href)").get()
        # # pega o título do artigo
        # title = article.css("a.tec--card__title__link::text").get()
        # # pega a data do artigo
        # date = article.css("span.tec--card__date::text").get()
        # # adiciona a notícia na lista
        # list_news.append({"url": url_notice, "title": title, "date": date})
        list_news.append(url_notice)

    return list_news


# Requisito 3
def scrape_next_page_link(html_content):

    page = Selector(html_content)
    next_page = page.css("a.tec--btn::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    news = {}
    news['url'] = selector.css("link[rel=canonical]::attr(href)").get()
    news['title'] = selector.css("h1.tec--article__header__title::text").get()
    news['timestamp'] = selector.css(
        "time.tec--article__header__date::text").get()

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
