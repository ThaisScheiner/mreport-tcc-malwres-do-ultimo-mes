import os
from fpdf import FPDF

# Diretório e caminho do PDF
pdf_dir = os.path.join(os.getcwd(), 'relatorios')
os.makedirs(pdf_dir, exist_ok=True)
PDF_OUTPUT = os.path.join(pdf_dir, 'relatorio_malwares.pdf')

# Apaga se já existir
if os.path.exists(PDF_OUTPUT):
    os.remove(PDF_OUTPUT)

# Caminho do arquivo de links
LINKS_TXT = os.path.join(pdf_dir, 'links_malware.txt')

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', size=14)
pdf.cell(200, 10, txt="Relatório de Malwares", ln=True, align='C')
pdf.set_font("Arial", size=12)
pdf.ln(10)

# Adicionando links ao PDF
if os.path.exists(LINKS_TXT):
    with open(LINKS_TXT, "r", encoding="utf-8") as f:
        links = f.readlines()
        for i, link in enumerate(links, 1):
            pdf.multi_cell(0, 10, txt=f"{i}. {link.strip()}")
else:
    pdf.cell(200, 10, txt="Nenhum link encontrado.", ln=True)

# Salvar o PDF
try:
    pdf.output(PDF_OUTPUT)
    print(f"✅ PDF gerado com sucesso em: {PDF_OUTPUT}")
except Exception as e:
    print(f"❌ Erro ao gerar o PDF: {e}")
