import subprocess
import os
import time

# Lista dos arquivos dos estágios
scripts = [
    "estagio0.py",
    "estagio1.py",
    "estagio2.py",
    "estagio3.py"
]

# Garantir que a pasta relatorios exista
os.makedirs("relatorios", exist_ok=True)

# Executa os estágios
for script in scripts:
    print(f"\n🔧 Executando {script}...")
    start = time.time()
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar {script}: {e}")
        break
    else:
        duration = time.time() - start
        print(f"✅ {script} executado com sucesso em {duration:.2f}s.")

# Executa a geração do PDF após os estágios, se tudo deu certo
else:
    print("\n📄 Gerando relatório em PDF...")
    try:
        subprocess.run(["python", "exportar_pdf.py"], check=True)
        print("✅ Relatório PDF gerado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao gerar o PDF: {e}")

print("\n🏁 Pipeline finalizado.")
