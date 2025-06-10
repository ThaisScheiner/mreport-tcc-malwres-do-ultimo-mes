import json
import os
import re

# Categorias expandidas com nomes populares e variações
CATEGORIAS = {
    'stealer': [
        'stealer', 'info-stealer', 'infostealer', 'eddiestealer', 'password stealer',
        'redline', 'raccoon', 'lummastealer', 'vidar', 'blackguard', 'hades', 'tycoon'
    ],
    'botnet': [
        'botnet', 'c2', 'command and control', 'zombie network', 'mirai', 'mozi',
        'qakbot', 'necurs', 'cutwail', 'asyncrat', 'cobalt strike'
    ],
    'ransomware': [
        'ransomware', 'encrypt', 'decryption', 'locker', 'data leak', 'double extortion',
        'lockbit', 'conti', 'revil', 'clop', 'alphv', 'blackcat', 'medusa'
    ],
    'trojan': [
        'trojan', 'backdoor', 'remote access', 'rat', 'keylogger', 'blended threat',
        'njrat', 'darkcomet', 'remcos', 'quasar', 'plugx', 'revenge rat'
    ],
    'exploit': [
        'exploit', 'exploit kit', 'kit de exploração', 'zero-day', 'n-day', 'cve-',
        'rce', 'remote code execution'
    ],
    'backdoor': [
        'backdoor', 'remote access', 'hidden access', 'covert access',
        'plugx', 'darkcomet', 'njrat', 'remcos', 'quasar', 'revenge rat',
        'netwire', 'nanocore', 'poison ivy', 'cobalt strike'
    ],
    'generico': [
        'malware', 'malicious software', 'malicious code'
    ]

}


def classificar_malware(texto):
    texto = texto.lower()
    encontrados = []
    for categoria, termos in CATEGORIAS.items():
        for termo in termos:
            # procura por palavra isolada usando \b
            if re.search(r'\b' + re.escape(termo.lower()) + r'\b', texto):
                encontrados.append(categoria)
                break  # Evita duplicatas
    return encontrados if encontrados else ['desconhecido']

def executar_classificacao(input_path='relatorios/relatorio.json', output_path='relatorios/relatorio_classificado.json'):
    with open(input_path, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    for arquivo, entidades in dados.items():
        texto = " ".join(entidades).lower()
        dados[arquivo] = {
            "entidades": entidades,
            "categorias": classificar_malware(texto)
        }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    print(f"Classificação salva em: {output_path}")

if __name__ == "__main__":
    executar_classificacao()
