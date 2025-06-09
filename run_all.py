import subprocess

print("\n===== EXECUTANDO TODOS OS ESTÁGIOS =====\n")

subprocess.run(["python", "estagio0.py"])          # coleta dos links
subprocess.run(["python", "estagio1.py"])          # download das paginas
subprocess.run(["python", "estagio2.py"])          # extrai do corpo
subprocess.run(["python", "estagio3.py"])          # limpeza de HTML
subprocess.run(["python", "estagio4.py"])          # classificacao
subprocess.run(["python", "estagio_tokenize.py"])  # tokenizacao
subprocess.run(["python", "estagio6.py"])          # gera os textos finais

print("\nTODOS OS ESTÁGIOS CONCLUÍDOS COM SUCESSO!\n")
