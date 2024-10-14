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

    # Seleciona os elem que contêm as URLs das notícias, ignorando o primeiro
    news_cards = selector.css("div.cs-overlay > a::attr(href)").getall()

    # Caso não encontre nenhuma URL, retorna uma lista vazia
    if not news_cards:
        return []

    # Retorna a lista de URLs das notícias
    return news_cards


# Requisito 3
def scrape_next_page_link(html_content):
    # Inicializa o objeto Selector com o conteúdo HTML
    selector = parsel.Selector(html_content)

    # Faz o scrape do link da próxima página
    next_page_url = selector.css("a.next.page-numbers::attr(href)").get()

    # Retorna a URL encontrada ou None, caso não exista
    return next_page_url if next_page_url else None


# Requisito 4
def scrape_news(html_content):
    selector = parsel.Selector(text=html_content)

    # Extraindo a URL da notícia
    url = selector.css('link[rel=canonical]::attr(href)').get()

    # Extraindo o título da notícia
    title = selector.css('h1.entry-title::text').get().strip()

    # Extraindo a data da notícia
    timestamp = selector.css('li.meta-date::text').get()

    # Extraindo o nome da pessoa autora
    writer = selector.css('span.author a::text').get()

    # Extraindo o tempo de leitura
    reading_time = int(
        selector.css('li.meta-reading-time::text').re_first(r'\d+')
        )

    # Extraindo o resumo
    summary = "".join(selector.css(
        'div.entry-content > p:first-of-type *::text'
        ).getall()).strip()

    # Extraindo a categoria
    category = selector.css('a.category-style span.label::text').get()

    # Criando o dicionário com as informações
    news_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }

    return news_data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
