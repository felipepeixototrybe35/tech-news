from tech_news.database import db


# Requisito 7
def search_by_title(title):
    # Cria uma expressão regular para busca case insensitive
    query = {"title": {"$regex": title, "$options": "i"}}

    # Faz a busca no banco de dados
    news = db.news.find(query)

    # Formata o resultado como uma lista de tuplas (título, url)
    result = [(item["title"], item["url"]) for item in news]

    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
