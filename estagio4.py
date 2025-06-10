import json
import os
import re

# Categorias expandidas com nomes populares e variações
CATEGORIAS = {
     'Stealer': [
        'RedLine', 'Raccoon', 'Vidar', 'BlackGuard', 'LummaStealer', 'EddieStealer', 'Tycoon'
    ],
    'Botnet': [
        'Mirai', 'Mozi', 'Qakbot', 'Necurs', 'Cutwail'
    ],
    'Ransomware': [
        'LockBit', 'Conti', 'REvil', 'Clop', 'ALPHV', 'BlackCat', 'Medusa'
    ],
    'Trojan': [
        'NjRAT', 'DarkComet', 'Remcos', 'Quasar', 'PlugX', 'RevengerAT'
    ],
    'Backdoor': [
        'NetWire', 'NanoCore', 'Poison Ivy', 'Cobalt Strike'  
    ],
    'RAT (Remote Access Trojan)': [
        'NjRAT', 'Quasar', 'DarkComet', 'Remcos', 'Xtreme RAT'
    ],
    'Keylogger': [
        'HawkEye', 'Phoenix', 'Snake'
    ],
    'Worm': [
        'Conficker', 'Morto', 'WannaCry'
    ],
    'Rootkit': [
        'ZeroAccess', 'Necurs', 'TDSS', 'Rustock'
    ],
    'Spyware': [
        'FinFisher', 'Pegasus'
    ],
    'Adware': [
        'Fireball', 'DealPly'
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
