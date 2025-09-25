def lerTxt(arquivo):
    with open (arquivo, "r") as txt:
        texto = ""
        for pagina in txt:
            texto += pagina
    print(texto)