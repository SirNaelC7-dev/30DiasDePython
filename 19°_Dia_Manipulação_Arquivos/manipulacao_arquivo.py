def contador(doc):
    texto = doc.read()

    linhas = len(texto.splitlines())
    palavras = len(texto.split())
    
    resultado = [linhas, palavras]

    return resultado



with open('nome_do_arquivo_para_contar_linhas_palavras') as doc:
    print(contador(doc))
