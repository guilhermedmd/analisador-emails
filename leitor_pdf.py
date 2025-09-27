import PyPDF2
from io import BytesIO

# arquivo = "Projetinho felas (3).pdf"

def lerPdf(arquivo):
    # with open(arquivo, "rb") as pdf:
    #     leitor_pdf = PyPDF2.PdfReader(pdf)
    #     texto = ""
    #     for pagina in leitor_pdf.pages:
    #         texto += pagina.extract_text()
    # print (texto)
    conteudo_bytes = arquivo.read()
    stream = BytesIO(conteudo_bytes)
    leitor_pdf = PyPDF2.PdfReader(stream)
    texto = ""
    for pag in leitor_pdf.pages:
        texto+= pag.extract_text()
    return texto