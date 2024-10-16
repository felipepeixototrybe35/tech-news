from datetime import datetime
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
    try:
        # Tenta converter a data do formato ISO para o formato dd/mm/AAAA
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d/%m/%Y")
    except ValueError:
        # Lança uma exceção caso a data seja inválida
        raise ValueError("Data inválida")

    # Faz a busca no banco de dados pela data formatada
    query = {"timestamp": formatted_date}
    news = db.news.find(query)

    # Formata o resultado como uma lista de tuplas (título, url)
    result = [(item["title"], item["url"]) for item in news]

    return result


# Requisito 9
def search_by_category(category):
    # Busca por categoria usando case insensitive com regex
    query = {"category": {"$regex": category, "$options": "i"}}

    # Faz a busca no banco de dados pelas notícias que correspondem à categoria
    news = db.news.find(query)

    # Formata o resultado como uma lista de tuplas (título, url)
    result = [(item["title"], item["url"]) for item in news]

    return result
