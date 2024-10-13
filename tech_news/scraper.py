import requests
import time
import parsel


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}

    try:
        # Faz a requisição HTTP GET
        response = requests.get(url, headers=headers, timeout=3)

        # Verifica se o status code é 200
        if response.status_code == 200:
            return response.text
        else:
            return None

    except requests.Timeout:
        # Retorna None se houver um timeout
        return None

    finally:
        # Aguarda 1 segundo antes de permitir uma nova requisição
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    # Inicializa o objeto Selector com o conteúdo HTML
    selector = parsel.Selector(html_content)

    # Seleciona os elementos que contêm as URLs das notícias, ignorando o primeiro (notícia em destaque)
    news_cards = selector.css("div.cs-overlay > a::attr(href)").getall()

    # Caso não encontre nenhuma URL, retorna uma lista vazia
    if not news_cards:
        return []

    # Retorna a lista de URLs das notícias
    return news_cards


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
