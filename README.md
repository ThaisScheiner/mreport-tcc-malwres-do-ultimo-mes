# 🧠 Projeto: mreport – Malware Report Automation

## 🔎 Visão Geral

**Objetivo**: Automatizar a busca por notícias recentes de malwares no site [bleepingcomputer.com](https://www.bleepingcomputer.com/news/security/), coletar os links relevantes e gerar um relatório em PDF com os resultados.

Este projeto simula um robô de monitoramento de ameaças, útil para profissionais de segurança da informação, pesquisadores, ou qualquer equipe que precise se manter informada sobre novos malwares.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia                | Finalidade                                                                          |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Python**                | Linguagem principal para automação e geração de relatórios.                         |
| **Selenium**              | Automação do navegador para simular um usuário acessando páginas e coletando dados. |
| **WebDriver Manager**     | Gerencia automaticamente o ChromeDriver.                                            |
| **FPDF**                  | Biblioteca leve para criação de PDFs.                                               |
| **Subprocess**            | Executa múltiplos scripts em sequência.                                             |
| **Chrome + ChromeDriver** | Navegador controlado automaticamente.                                               |

---

## 🧩 Estrutura do Projeto

```
mreport/
├── estagio0.py           # Coleta de links de notícias de malware
├── estagio1.py           # (em branco ou futura lógica adicional)
├── estagio2.py           # (em branco ou futura lógica adicional)
├── estagio3.py           # (em branco ou futura lógica adicional)
├── exportar_pdf.py       # Geração do relatório PDF
├── run_all.py            # Pipeline principal que executa todos os scripts
└── relatorios/           # Pasta de saída onde o PDF é salvo
```

---

## 🧪 Explicações

### 🔧 estagio0.py

- Acessa a página de notícias de segurança.
- Espera elementos com links contendo "malware".
- Coleta e imprime os links.
- Fecha o navegador automaticamente.

### 📄 exportar_pdf.py

- Cria a pasta `relatorios/` se não existir.
- Cria um novo PDF com o título “Relatório de Malwares”.
- Pode ser estendido para incluir links.
- Salva o PDF como `relatorio_malwares.pdf`.

### 🔁 run_all.py

- Executa os arquivos `estagio0.py`, `estagio1.py`, `estagio2.py`, `estagio3.py` em sequência.
- Gera o PDF se tudo ocorrer bem.

---

## 💼 Importância do Projeto

- Simula um robô de coleta automatizada de ameaças de segurança.
- Demonstra conhecimento em automação web, extração de dados e geração de relatórios.
- Aplicável em contextos reais de monitoramento e resposta a incidentes.

## Instalações para o projeto

C:\Windows\system32>python.exe -m pip install --upgrade pip

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
