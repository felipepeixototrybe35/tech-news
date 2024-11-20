Este projeto é fruto do curso de Desenvolvedor Web FullStack da Trybe, por isso vem separado por requisitos.

Requisito 1 >> Função `fetch` em `tech_news/scraper.py`
Esta função é responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.
A função recebe uma URL
A função faz uma requisição HTTP `get` para esta URL utilizando a função `requests.get`
A função retorna o conteúdo HTML da resposta.
A função tem um Rate Limit de 1 requisição por segundo; Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo entre cada   requisição que fizer.
Caso a requisição seja bem sucedida com `Status Code 200: OK`, será retornado seu conteúdo de texto;
Caso a resposta tenha o código de status diferente de `200`, retornará `None`;
Caso a requisição não receba resposta em até 3 segundos, ela deve ser abandonada (este caso é conhecido como "Timeout") e a função retorna None.

Requisito 2 >> Função `scrape_updates` em `tech_news/scraper.py`
Esta função fará o scrape da página para obter as URLs das páginas de notícias. Vamos utilizar ferramentas como a biblioteca Parsel, para obter os dados de cada página.
A função recebe uma string com o conteúdo HTML da página inicial do blog
A função faz o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
A função retorna o conteúdo HTML da resposta.
A notícia em destaque da primeira página não está inclusa, apenas as notícias dos cards.
A função retorna esta lista.
Caso não encontre nenhuma URL de notícia, a função retorna uma lista vazia.

Requisito 3 >> Função `scrape_next_page_link` em `tech_news/scraper.py`
Esta função será responsável por fazer o scrape do link da próxima página.
A função recebe como parâmetro uma string contendo o conteúdo HTML da página de novidades
A função faz o scrape deste HTML para obter a URL da próxima página.
A função retorna a URL obtida.
Caso não encontre o link da próxima página, a função retorna `None`

Requisito 4 >> Função `scrape_news` em `tech_news/scraper.py`
Esta função faz o scrape dos dados que procuramos!
A função recebe como parâmetro o conteúdo HTML da página de uma única notícia.
No conteúdo recebido, a função busca as informações das notícias para preencher um dicionário com os seguintes atributos:
  * `url` - link para acesso da notícia.
  * `title` - título da notícia.
  * `timestamp` - data da notícia, no formato `dd/mm/AAAA`.
  * `writer` - nome da pessoa autora da notícia.
  * `reading_time` - número de minutos necessários para leitura.
  * `summary` - o primeiro parágrafo da notícia.
  * `category` - categoria da notícia.

>>Do Requisito 5 em diante, o MongoDB é utilizado via Docker. Mais detalhes no arquivo `docker-compose.yml`<<

Requisito 5 >> Função `get_tech_news` em `tech_news/scraper.py`
A função recebe como parâmetro um número inteiro `n` e busca as últimas `n` notícias do site.
Utilizando as funções `fetch`, `scrape_updates`, `scrape_next_page_link` e `scrape_news` para buscar as notícias e processar seu conteúdo.
As notícias buscadas são inseridas no MongoDB;
Após inserir as notícias no banco, a função retorna estas mesmas notícias.

Requisito 6 >>
