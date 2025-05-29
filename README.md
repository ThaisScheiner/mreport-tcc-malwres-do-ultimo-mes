
# 🛡️ Projeto de Coleta Automatizada de Notícias sobre Malwares — Maio de 2025

## 📌 Objetivo

Este projeto tem como objetivo automatizar a busca por notícias recentes relacionadas a malwares mais impactantes do último mês (Maio de 2025), capturando os links dos resultados de busca e salvando-os para análises futuras.

Trata-se de uma ferramenta de **inteligência automatizada para cibersegurança**, essencial para monitorar as tendências de ameaças digitais em tempo real, com foco em **malwares emergentes**.

---

## 🧠 Motivação e Importância

Com o crescente aumento de ameaças digitais, como ransomwares, spywares e trojans, é vital manter-se atualizado sobre os malwares mais impactantes. A proposta deste projeto é reduzir o trabalho manual de buscas e oferecer um **relatório automatizado e rápido** dos links mais relevantes, auxiliando analistas, pesquisadores e profissionais de segurança da informação.

Essa automação:

- Economiza tempo na triagem de fontes.
- Centraliza informações para investigações posteriores.
- Permite futuras integrações com análise de texto, classificadores de ameaça e dashboards.

---

## ⚙️ Tecnologias Utilizadas

### ✅ Python 3

Escolhido por ser uma linguagem de fácil leitura, ampla comunidade e suporte a bibliotecas robustas de automação, scraping e manipulação de arquivos.

Vantagens do Python no projeto:
- Sintaxe limpa e acessível.
- Ampla compatibilidade com bibliotecas como Selenium e Pandas.
- Ideal para automações e protótipos rápidos de coleta de dados.

### ✅ Selenium WebDriver

Ferramenta utilizada para simular a navegação em um navegador real (Chrome), acessar páginas de busca e interagir com seus elementos.

Funções usadas:
- `driver.get(url)` para acessar a página.
- `find_elements()` para buscar os links das notícias.
- `WebDriverWait` para aguardar carregamento completo da página.

### ✅ WebDriver Manager

Gerencia automaticamente o download e configuração do ChromeDriver adequado à versão instalada do Chrome. Isso evita problemas de incompatibilidade entre navegador e driver.

### ✅ Bing Search

Devido a restrições impostas pelo Google (como reCAPTCHA), optei por utilizar o mecanismo de busca Bing, que oferece:
- Maior permissividade para automações.
- Interface amigável à coleta de links com estrutura HTML mais acessível.
- Resultados relevantes e diversificados sobre o tema pesquisado.

---

## 🔍 Termo de Pesquisa Utilizado

```
malwares mais afetados em maio de 2025
```

Este termo busca localizar os artigos mais recentes com foco nos malwares com maior impacto no mês de referência.

---

## 🗂️ Estrutura de Arquivos

```
.
├── estagio0.py                   # Script principal de coleta de links de notícias
├── relatorios/
│   └── links_malware_bing.txt   # Arquivo com os links salvos automaticamente
├── README.md                     # Documentação do projeto
```

---

## 📁 Estrutura do Projeto

```
mreport/
│
├── browser/                      # Scrapers por fonte
│   ├── browser.py                # WebDriver e navegação
│   ├── thn.py                    # Scraper para The Hacker News
│   └── wiki.py                   # (Opcional) Scraper para Wikipedia
│
├── core/                         # Estágios principais do processo
│   ├── estagio0.py # Coleta de links no Bing
│   ├── estagio1.py     # Extração de conteúdo das notícias
│   ├── estagio2.py   # Combinação dos textos extraídos
│   └── estagio3.py      # Análise textual (opcional)
│
├── reports/                      # Arquivos de saída
│   ├── links_malware_bing.txt
│   ├── links_malware.txt
│   └── relatorio_malwares.pdf
│
├── utils/                        # Utilitários e exportação
│   ├── exportar_pdf.py          # Geração de relatório em PDF
│   └── utilitario.py            # Funções auxiliares
│
├── venv/                         # Ambiente virtual Python
│
├── run_all.py                    # Roda todos os estágios automaticamente
├── instalacoes_no_py.txt         # Lista de dependências
└── README.md                     # Documentação do projeto
```

### `estagio0.py` – Coleta de Links via Bing
- Realiza a pesquisa de notícias relacionadas a malwares mais prevalentes do mês de maio de 2025 usando o Bing.
- Filtra os links que contenham a palavra "malware".
- Salva os links únicos em um arquivo `.txt` (`relatorios/links_malware.txt`).

### `estagio1.py` – Captura das Notícias
- Acessa cada link coletado no estágio 0.
- Captura o conteúdo HTML da notícia.
- (Opcional) Salva as páginas em PDF usando bibliotecas como `pdfkit`.

### `estagio2.py` – Combinação e Organização
- Concatena os arquivos de texto ou PDFs gerados anteriormente.
- Gera um único relatório contendo todas as informações.
- Organiza por data ou relevância.

### `estagio3.py` – Análise de Conteúdo (opcional)
- Realiza análise textual dos conteúdos coletados.
- Extrai palavras-chave, menções de tipos de malware, países afetados, etc.
- Pode incluir gráficos ou sumarização via NLP.

### `utilitario.py` – Funções de Apoio
- Contém funções auxiliares utilizadas nos outros estágios.
- Exemplo: salvar em PDF, limpar HTML, formatar texto, etc.

---

## 📥 Saída do Script

- Uma lista única de links relacionados a malwares do mês desejado.
- O arquivo `links_malware_bing.txt` contém os resultados em formato `.txt`, um por linha.

---


## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, sugestões de termos de pesquisa ou novos motores de busca.

---

## Instalações para o projeto

```bash
pip3 install nltk
```

```bash
pip install webdriver-manager
```

```bash
pip install selenium webdriver-manager nltk spacy
```

```bash
python -m nltk.downloader punkt
```

```bash
python -m spacy download en_core_web_sm
```

```bash
pip install fpdf
```

```bash
pip install python_anticaptcha
```
