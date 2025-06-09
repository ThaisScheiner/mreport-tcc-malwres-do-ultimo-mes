# estagio4.py
import json
import os

CATEGORIAS = {
    'stealer': ['stealer', 'info-stealer', 'eddiestealer', 'password'],
    'minerador': ['crypto', 'miner', 'cryptojacking'],
    'apt': ['apt', 'espionage', 'advanced persistent threat'],
    'botnet': ['botnet', 'c2', 'command and control'],
    'ransomware': ['ransomware', 'encrypt', 'decryption'],
    'trojan': ['trojan', 'backdoor', 'remote access'],
}

def classificar_malware(texto):
    texto = texto.lower()
    encontrados = []
    for categoria, termos in CATEGORIAS.items():
        for termo in termos:
            if termo in texto:
                encontrados.append(categoria)
                break
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
