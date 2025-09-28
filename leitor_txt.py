def lerTxt(arquivo):
    conteudo_bytes = arquivo.read()
    texto = conteudo_bytes.decode("utf-8")      
    return texto