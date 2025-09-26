from flask import Flask, render_template,request
import leitor_pdf
import leitor_txt
import gemini_api

# leitorPdf.lerPdf("Projetinho felas (3).pdf")
# conteudo_email = leitor_txt.lerTxt("emailImp.txt")
# gemini_api.avaliar_email(conteudo_email)

app = Flask(__name__)

@app.route("/")
def pagina():
    return render_template("index.html")

@app.route("/enviararquivo", methods = ['POST'])
def enviarEmail():
    arquivo = request.files['arquivo']
    if arquivo.filename.endswith(".pdf"):
        conteudo = leitor_pdf.lerPdf(arquivo)
        gemini_api.avaliar_email(conteudo)
        return render_template("index.html")
    elif arquivo.filename.endswith(".txt"):
        conteudo = leitor_txt.lerTxt(arquivo)
        gemini_api.avaliar_email(conteudo)
        return render_template("index.html")    

if __name__ == "__main__":
    app.run(debug=True)




