Scielo Scraper GUI (customtkinter)
=================================

Este arquivo descreve como executar a interface gráfica que facilita o uso do scraper `scielo_v2.buscar_scielo`.

Dependências mínimas
---------------------
- Python 3.10+ compatível com o projeto
- customtkinter (pip install customtkinter)
- selenium (ver `requirements.txt` do scraper)
- Firefox e geckodriver disponíveis no PATH

Instalação rápida
-----------------
1. Ative seu ambiente virtual (se usado).
2. Instale dependências:

```
pip install customtkinter
pip install -r c:\Users\PC\acervo_digital\biblioteca\scielo\scraping_scielo\requirements.txt
```

Executando a GUI
-----------------
Na pasta `scraping_scielo` execute:

```
python gui.py
```

Uso
---
Digite o termo de pesquisa e clique em "Pesquisar". A GUI executará o scraper em segundo plano (thread) e exibirá os resultados. Clicar em "Abrir link" abrirá o link no navegador.

Notas
-----
- A execução do scraper pode demorar (Selenium + download). Use com cuidado em ambientes de produção.
- Se ocorrerem erros relacionados ao web driver, verifique se o geckodriver está instalado e no PATH.
