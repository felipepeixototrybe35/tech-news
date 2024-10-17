from tech_news.database import db


# Requisito 10
def top_5_categories():
    # Pipeline de agregação para contar as ocorrências de cada categoria
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},  # Ordena por contagem decrescente e, em caso de empate, por ordem alfabética
        {"$limit": 5}  # Limita o resultado às top 5 categorias
    ]

    # Executa o pipeline de agregação no MongoDB
    top_categories = list(db.news.aggregate(pipeline))

    # Extrai as categorias do resultado
    result = [category["_id"] for category in top_categories]

    return result
