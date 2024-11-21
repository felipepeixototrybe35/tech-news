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
Esta função faz o scrape da página para obter as URLs das páginas de notícias. Vamos utilizar ferramentas como a biblioteca Parsel, para obter os dados de cada página.
A função recebe uma string com o conteúdo HTML da página inicial do blog
A função faz o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
A função retorna o conteúdo HTML da resposta.
A notícia em destaque da primeira página não está inclusa, apenas as notícias dos cards.
A função retorna esta lista.
Caso não encontre nenhuma URL de notícia, a função retorna uma lista vazia.

Requisito 3 >> Função `scrape_next_page_link` em `tech_news/scraper.py`
Esta função é responsável por fazer o scrape do link da próxima página.
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

Requisito 6 >> Testa a classe `ReadingPlanService` em `tests/reading_plan/test_reading_plan.py`
O serviço de **planejamento de leituras**, implementado no arquivo `tech_news/analyzer/reading_plan.py`, coleta as notícias do banco de dados e as divide em 2 agrupamentos:
  1. `readable`: notícias que podem ser lidas em até `X` minutos
  2. `unreadable`: notícias que **não** podem ser lidas em até `X` minutos
Além disso, as notícias `readable` são organizadas em sub-grupos cuja soma dos tempos de leitura seja menor que `X`. Assim, a pessoa leitora pode ler mais do que 1 notícia sem ultrapassar o tempo disponível!
O valor de `X`, que é o tempo de leitura que uma pessoa tem disponível, é passado por parâmetro no método `group_news_for_available_time`, que é um **método de classe**.
O teste valida que uma exceção é levantada se o método é chamado com parâmetro de valor inválido
O teste valida que os valores 'unfilled_time' retornados estão corretos
O teste valida que os valores em 'readable' retornados estão corretos
O teste valida que os valores em 'unreadable' estão corretos

Requisito 7 >> Função `search_by_title` em `tech_news/analyzer/search_engine.py`
Esta função é responsável por realizar buscas por título.
A função recebe uma string com um título de notícia.
A função busca as notícias do banco de dados por título.
A função retorna uma lista de tuplas com as notícias encontradas nesta busca.  

Requisito 8 >> Função `search_by_date` em `tech_news/analyzer/search_engine.py`
Esta função busca as notícias do banco de dados por data.
A função recebe como parâmetro uma data no formato ISO `AAAA-mm-dd`.
A função deve buscar as notícias do banco de dados por data (formato `dd/mm/AAAA`).
A função retorna no mesmo formato do requisito anterior.
Caso a data seja inválida, ou esteja em outro formato, uma exceção `ValueError` é lançada com a mensagem `Data inválida`.
Caso nenhuma notícia seja encontrada, retorna uma lista vazia.

Requisito 9 >> Função `search_by_category` em `tech_news/analyzer/search_engine.py`
Esta função busca as notícias do banco de dados por categoria.
A função recebe como parâmetro o nome da categoria completo.
A função retorna no mesmo formato do requisito anterior.
Caso nenhuma notícia seja encontrada, retorna uma lista vazia.
A busca é _case insensitive_.

Requisito 10 >> Função `top_5_categories` em `tech_news/analyzer/ratings.py`
Esta função lista as cinco categorias com maior ocorrência no banco de dados.
A função deve buscar as categorias do banco de dados e calcular a sua "popularidade" com base no número de ocorrências;
As top 5 categorias da análise são retornadas em uma lista no formato `["category1", "category2"]`;
A ordem das categorias retornadas é da mais popular para a menos popular, ou seja, categorias que estão em mais notícias primeiro;
Em caso de empate, o desempate deve é por ordem alfabética de categoria.
Caso haja menos de cinco categorias, no banco de dados, retorna todas as categorias existentes;
Caso não haja categorias disponíveis, retorna uma lista vazia.
