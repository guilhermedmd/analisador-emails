import PyPDF2
from io import BytesIO

def lerPdf(arquivo):
    conteudo_bytes = arquivo.read()
    stream = BytesIO(conteudo_bytes)
    leitor_pdf = PyPDF2.PdfReader(stream)
    texto = ""
    for pag in leitor_pdf.pages:
        texto+= pag.extract_text()
    return texto