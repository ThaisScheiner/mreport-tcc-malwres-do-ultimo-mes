import os
from fpdf import FPDF

def gerar_pdf_com_links(lista_dados):
    if not lista_dados:
        print("❌ Nenhum dado para gerar o PDF.")
        return

    pdf_dir = os.path.join(os.getcwd(), 'relatorios')
    os.makedirs(pdf_dir, exist_ok=True)
    PDF_OUTPUT = os.path.join(pdf_dir, 'relatorio_malwares.pdf')

    if os.path.exists(PDF_OUTPUT):
        os.remove(PDF_OUTPUT)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=14)
    pdf.cell(200, 10, txt="Relatório de Malwares - Maio 2025", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    for i, (titulo, data, link) in enumerate(lista_dados, 1):
        pdf.set_font("Arial", 'B', size=12)
        pdf.multi_cell(0, 10, txt=f"{i}. {titulo}")
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 8, txt=f"Data: {data}")
        pdf.set_text_color(0, 0, 255)
        pdf.multi_cell(0, 8, txt=f"Link: {link}")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(5)
        pdf.cell(0, 0, '', ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

    try:
        pdf.output(PDF_OUTPUT)
        print(f"✅ PDF gerado com sucesso em: {PDF_OUTPUT}")
    except Exception as e:
        print(f"❌ Erro ao gerar o PDF: {e}")
