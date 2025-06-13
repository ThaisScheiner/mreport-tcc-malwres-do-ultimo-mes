import os
import re
import json

# Base de classificação de malwares
BASE_MALWARE = {
    "worm": "Worm", "conficker": "Worm", "autorun": "Worm",
    "trojan": "Trojan", "trojanized": "Trojan", "banker": "Trojan", "dropper": "Trojan",
    "exploit": "Exploit", "zero-day": "Exploit", "0day": "Exploit", "cve": "Exploit",
    "ransomware": "Ransomware", "locker": "Ransomware", "crypto": "Ransomware", "encryptor": "Ransomware",
    "decryptor": "Ransomware", "wannacry": "Ransomware", "lockbit": "Ransomware", "revil": "Ransomware",
    "spyware": "Spyware", "keylogger": "Spyware", "logger": "Spyware", "snooper": "Spyware",
    "adware": "Adware", "popup": "Adware", "ads": "Adware",
    "rootkit": "Rootkit", "bootkit": "Rootkit", "stealth": "Rootkit",
    "virus": "Virus", "infection": "Virus", "infected": "Virus", "macro": "Virus", "file-infector": "Virus",
    "backdoor": "Backdoor", "remote-access": "Backdoor", "rat": "Backdoor",
    "builder": "Backdoor", "revshell": "Backdoor", "bindshell": "Backdoor"
}

def classificar_texto(texto, base_malware):
    texto = texto.lower()
    palavras = re.findall(r'\b[\w-]+\b', texto)  # <- preserva hífens
    classificacoes = []
    palavras_encontradas = set()

    for palavra in palavras:
        if palavra in base_malware and palavra not in palavras_encontradas:
            classificacoes.append({
                "classificacao": palavra,
                "categoria": base_malware[palavra]
            })
            palavras_encontradas.add(palavra)

    return classificacoes

def processar_pasta(diretorio, resultado):
    if not os.path.exists(diretorio):
        print(f"[ERRO] Pasta não encontrada: {diretorio}")
        return

    arquivos_txt = [f for f in os.listdir(diretorio) if f.endswith(".txt")]
    if not arquivos_txt:
        print(f"[AVISO] Nenhum arquivo .txt encontrado em: {diretorio}")
        return

    for nome_arquivo in arquivos_txt:
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            texto = f.read()

        texto_limpo = re.sub(r"[^\w\s-]", " ", texto)  # <- preserva hífens
        classificacoes = classificar_texto(texto_limpo, BASE_MALWARE)

        resultado[nome_arquivo] = {
            "classificacoes": classificacoes
        }

        status = "[OK]" if classificacoes else "[AVISO]"
        print(f"{status} {nome_arquivo} -> {len(classificacoes)} classificação(ões).")

def main():
    resultado = {}

    # Diretórios que contêm os arquivos .txt a serem classificados
    pastas_para_processar = [
        r"C:\Temp\tokenize",  # arquivos convertidos de HTML
        r"C:\Users\Thais\Desktop\mreport\relatorios\textos_finais"
    ]

    for pasta in pastas_para_processar:
        processar_pasta(pasta, resultado)

    # Gera JSON de saída
    pasta_saida = r"C:\Users\Thais\Desktop\mreport\relatorios"
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_json = os.path.join(pasta_saida, "relatorio_classificado.json")

    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"\n[OK] Arquivo relatorio_classificado.json salvo em:\n{caminho_json}")

if __name__ == "__main__":
    main()
