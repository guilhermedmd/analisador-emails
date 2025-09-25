import PyPDF2

# arquivo = "Projetinho felas (3).pdf"

def lerPdf(arquivo):
    with open(arquivo, "rb") as pdf:
        leitor_pdf = PyPDF2.PdfReader(pdf)
        texto = ""
        for pagina in leitor_pdf.pages:
            texto += pagina.extract_text()
    print (texto)