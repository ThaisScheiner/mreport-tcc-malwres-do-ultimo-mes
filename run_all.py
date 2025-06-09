import subprocess

print("\n===== EXECUTANDO TODOS OS ESTÁGIOS =====\n")

subprocess.run(["python", "estagio0.py"])   # Coleta dos links
subprocess.run(["python", "estagio1.py"])   # Download das páginas
subprocess.run(["python", "estagio2.py"])   # Extração do corpo
subprocess.run(["python", "estagio3.py"])   # Limpeza de HTML
subprocess.run(["python", "estagio4.py"])   # Classificação
subprocess.run(["python", "estagio_tokenize.py"])  # Tokenização
subprocess.run(["python", "estagio6.py"])   # Geração dos textos finais

print("\n🎉 TODOS OS ESTÁGIOS CONCLUÍDOS COM SUCESSO!\n")
