import json
from collections import defaultdict
import os

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
            print(f"[✔] Relatório salvo em: {caminho_saida}\n")
        else:
            print(f"[❌] Falha ao salvar o relatório.\n")

if __name__ == "__main__":
    gerar_relatorio()
