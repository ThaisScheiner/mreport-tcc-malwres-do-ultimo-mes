import os
import re
import json

# Base de classificação de malwares
BASE_MALWARE = {
    # Worms
    "worm": "Worm",
    "conficker": "Worm",
    "autorun": "Worm",

    # Trojans
    "trojan": "Trojan",
    "trojanized": "Trojan",
    "banker": "Trojan",
    "dropper": "Trojan",

    # Exploits
    "exploit": "Exploit",
    "zero-day": "Exploit",
    "0day": "Exploit",
    "cve": "Exploit",

    # Ransomware
    "ransomware": "Ransomware",
    "locker": "Ransomware",
    "crypto": "Ransomware",
    "encryptor": "Ransomware",
    "decryptor": "Ransomware",
    "wannacry": "Ransomware",
    "lockbit": "Ransomware",
    "revil": "Ransomware",

    # Spyware
    "spyware": "Spyware",
    "keylogger": "Spyware",
    "logger": "Spyware",
    "snooper": "Spyware",

    # Adware
    "adware": "Adware",
    "popup": "Adware",
    "ads": "Adware",

    # Rootkits
    "rootkit": "Rootkit",
    "bootkit": "Rootkit",
    "stealth": "Rootkit",

    # Virus
    "virus": "Virus",
    "infection": "Virus",
    "infected": "Virus",
    "macro": "Virus",
    "file-infector": "Virus",

    # Backdoors
    "backdoor": "Backdoor",
    "remote-access": "Backdoor",
    "rat": "Backdoor",
    "builder": "Backdoor",
    "revshell": "Backdoor",
    "bindshell": "Backdoor"
}

def classificar_texto(texto, base_malware):
    texto = texto.lower()
    palavras = re.findall(r'\b\w+\b', texto)
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
        print(f"Pasta não encontrada: {diretorio}")
        return

    arquivos_txt = [f for f in os.listdir(diretorio) if f.endswith(".txt")]
    if not arquivos_txt:
        print(f"Nenhum arquivo .txt encontrado em: {diretorio}")
        return

    for nome_arquivo in arquivos_txt:
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            texto = f.read()

        texto_limpo = re.sub(r"[^\w\s]", " ", texto)
        classificacoes = classificar_texto(texto_limpo, BASE_MALWARE)

        resultado[nome_arquivo] = {
            "classificacoes": classificacoes
        }

        status = "[OK]" if classificacoes else "[AVISO]"
        print(f"{status} {nome_arquivo} -> {len(classificacoes)} classificações.")

def main():
    resultado = {}

    # Pastas a serem processadas - inclua a pasta textos_finais para classificar também os arquivos lá
    pastas_para_processar = [
        r"C:\Temp\tokenize",
        r"C:\Temp\paginas",
        r"C:\Users\Thais\Desktop\mreport\relatorios\textos_finais"
    ]

    for pasta in pastas_para_processar:
        processar_pasta(pasta, resultado)

    # Caminho de saída do JSON
    pasta_saida = r"C:\Users\Thais\Desktop\mreport\relatorios"
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_json = os.path.join(pasta_saida, "relatorio_classificado.json")

    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"\nArquivo relatorio_classificado.json criado em:\n{caminho_json}")

if __name__ == "__main__":
    main()
