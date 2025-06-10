# utilitario.py
import json
import os

class Utilitario:
    @staticmethod
    def salvar(estagio, dados, nome_arquivo="resultado.json"):
        pasta = "relatorios"
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, nome_arquivo)
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        print(f"Estágio {estagio} salvo em: {caminho}")
