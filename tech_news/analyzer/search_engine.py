import datetime
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    news_list = []
    # https://www.guru99.com/regular-expressions-mongodb.html
    for news in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        new = news['title'], news['url']
        news_list.append(new)
    return news_list


def date_validator(string):
    try:
        datetime.datetime.strptime(string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# Requisito 7
def search_by_date(date):
    date_validation = date_validator(date)
    news_list = []

    if date_validation:
        for new in db.news.find({
                "timestamp": {"$regex": date, "$options": "i"}}):
            notice = new["title"], new["url"]
            news_list.append(notice)
        return news_list
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
