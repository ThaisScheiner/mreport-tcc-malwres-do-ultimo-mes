import json
from collections import defaultdict
import os
import re

# Diretório onde estão os arquivos txt tokenizados
TOKENIZE_DIR = r"C:\Temp\tokenize"

def adicionar_classificacao_nos_txt(dados, diretorio=TOKENIZE_DIR):
    """
    Para cada arquivo .txt no diretório, atualiza o arquivo acrescentando
    a seção de classificações encontradas naquele arquivo.
    """
    if not os.path.exists(diretorio):
        print(f"[ERRO] Diretório para atualizar TXT não encontrado: {diretorio}")
        return

    arquivos_txt = [f for f in os.listdir(diretorio) if f.endswith(".txt")]

    for nome_arquivo in arquivos_txt:
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        classificacoes = dados.get(nome_arquivo, {}).get("classificacoes", [])

        # Lê o conteúdo original
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        # Remove qualquer seção antiga "=== CLASSIFICAÇÕES DETECTADAS ===" para evitar duplicação
        conteudo_limpo = re.split(r"\n=== CLASSIFICAÇÕES DETECTADAS ===\n", conteudo)[0]

        # Cria texto da seção classificações
        secao = "\n\n=== CLASSIFICAÇÕES DETECTADAS ===\n"
        if classificacoes:
            for c in classificacoes:
                secao += f"- {c['classificacao']} ({c['categoria']})\n"
        else:
            secao += "Nenhuma classificação encontrada.\n"

        # Escreve o arquivo novamente com a seção adicionada
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo_limpo + secao)

        print(f"[ATUALIZADO] {nome_arquivo} com classificações.")

def gerar_relatorio(path=r"C:\Users\Thais\Desktop\mreport\relatorios\relatorio_classificado.json", salvar_em_txt=True):
    if not os.path.exists(path):
        print(f"[ERRO] Arquivo JSON não encontrado: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    resumo = defaultdict(list)

    for arquivo, info in dados.items():
        for classificacao in info.get("classificacoes", []):
            categoria = classificacao.get("categoria", "Desconhecido")
            nome = classificacao.get("classificacao", "Não identificado")
            resumo[categoria].append((nome, arquivo))

    print("\nRELATÓRIO FINAL DOS MALWARES")
    print("=================================================\n")

    linhas_txt = []

    for categoria, ocorrencias in resumo.items():
        cabecalho = f"Categoria: {categoria.upper()} - {len(ocorrencias)} ocorrência(s)\n"
        print(cabecalho.strip())
        linhas_txt.append(cabecalho)

        for classificacao, arquivo in ocorrencias:
            linha = f"  - {classificacao} (Arquivo: {arquivo})"
            print(linha)
            linhas_txt.append(linha)
        print()
        linhas_txt.append("")

    if salvar_em_txt:
        caminho_textos = r"C:\Users\Thais\Desktop\mreport\relatorios\textos_finais"
        os.makedirs(caminho_textos, exist_ok=True)
        caminho_saida = os.path.join(caminho_textos, "relatorio_final.txt")
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write("\n".join(linhas_txt))

        if os.path.exists(caminho_saida):
            print(f"[OK] Relatório salvo em: {caminho_saida}\n")
        else:
            print(f"[ERRO] Falha ao salvar o relatório.\n")

    # Atualiza os arquivos txt no diretório tokenize para incluir a classificação detectada
    adicionar_classificacao_nos_txt(dados)

if __name__ == "__main__":
    gerar_relatorio()
