# estagio5.py
import json
from collections import defaultdict

def gerar_relatorio(path='relatorios/relatorio_classificado.json'):
    with open(path, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    resumo = defaultdict(list)

    for arquivo, info in dados.items():
        for categoria in info.get("categorias", []):
            resumo[categoria].append(arquivo)

    print("\nRELATÓRIO FINAL DOS MALWARES")
    print("=================================================\n")

    for categoria, arquivos in resumo.items():
        print(f"Categoria: {categoria.upper()} - {len(arquivos)} ocorrência(s)")
        for arq in arquivos:
            print(f"  - {arq}")
        print()

    print("Relatório completo.\n")

if __name__ == "__main__":
    gerar_relatorio()
