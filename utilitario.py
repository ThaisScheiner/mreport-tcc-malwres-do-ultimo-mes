import os, json

class Utilitario:
    @staticmethod
    def arquivo(estagio):
        pasta_estagio = f"./arquivos/estagio{estagio}"
        os.makedirs(pasta_estagio, exist_ok=True)  # Garante que o diretório existe

        arr = os.listdir(pasta_estagio)
        if len(arr) > 0:
            with open(os.path.join(pasta_estagio, arr[0]), "r") as f:
                buffer = json.load(f)
                buffer['nome'] = arr[0]
                return buffer
        return None

    @staticmethod
    def salvar(estagio, js, nome):
        pasta_estagio = f"./arquivos/estagio{estagio}"
        os.makedirs(pasta_estagio, exist_ok=True)  # Garante que o diretório existe

        with open(os.path.join(pasta_estagio, nome), "w") as f:
            json.dump(js, f, indent=2, ensure_ascii=False)
        return True
