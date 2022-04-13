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
        # https://docs.python.org/pt-br/3/library/datetime.html
        datetime.datetime.strptime(string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# Requisito 7
def search_by_date(date):
    date_validation = date_validator(date)
    news_list = []

    if date_validation:
        # https://www.guru99.com/regular-expressions-mongodb.html
        for new in db.news.find({
                "timestamp": {"$regex": date, "$options": "i"}}):
            notice = new["title"], new["url"]
            news_list.append(notice)
        return news_list
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news_list = []
    # https://www.mongodb.com/docs/manual/reference/operator/query/elemMatch/
    # elemMatch retorna as notí que contenham a string no source
    for new in db.news.find({
           "sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}):
        item = new["title"], new["url"]
        news_list.append(item)
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
