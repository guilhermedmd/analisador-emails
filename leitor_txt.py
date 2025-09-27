def lerTxt(arquivo):
    # with open (arquivo, "r") as txt:
    #     texto = ""
    #     for pagina in txt:
    #         texto += pagina
    # return texto
    conteudo_bytes = arquivo.read()
    texto = conteudo_bytes.decode("utf-8")      
    return texto