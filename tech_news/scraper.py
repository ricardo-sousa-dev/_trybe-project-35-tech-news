import re
import requests  # importa o módulo requests para fazer a requisição HTTP
import time  # importa o módulo time para simular um delay
from parsel import Selector  # importa o módulo parsel para fazer parse do HTML
import database  # módulo database para inserir os dados no banco de dados


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
    news['title'] = selector.css("#js-article-title::text").get()
    news['timestamp'] = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css("a.tec--author__info__link::text").get()
    if writer is None:
        writer = selector.css(
            "div.tec--timestamp div:nth-child(2) a::text").get()
        if writer is None:
            writer = selector.css("p.z--m-none::text").get()
    news['writer'] = writer.strip() if writer is not None else None

    shares_count = selector.css("div.tec--toolbar__item::text").get()
    if shares_count:
        # https://pythonexamples.org/python-regex-extract-find-all-the-numbers-in-string/
        shares_count = int(re.findall(r'\d+', shares_count)[0])
    else:
        shares_count = 0
    news['shares_count'] = shares_count

    news['comments_count'] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
        )
    # https://stackoverflow.com/questions/64402251/difference-between-get-and-getall-in-scrapy-and-interpreting-code-output
    # https://www.w3schools.com/python/ref_string_join.asp
    news['summary'] = ''.join(selector.css(
        "div.tec--article__body > p:nth-child(1) *::text").getall()
        )
    # https://www.w3schools.com/python/ref_string_strip.asp
    sources = selector.css("div.z--mb-16 div a::text").getall()
    news['sources'] = [source.strip() for source in sources]

    categories = selector.css("div#js-categories a::text").getall()
    news['categories'] = [category.strip() for category in categories]

    return news


# Requisito 5
def get_tech_news(amount):
    """Retorna uma lista de notícias"""

