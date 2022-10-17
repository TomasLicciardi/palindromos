def palindromo(palabra):

    frase = palabra.replace(" ","")
    frase = frase.lower()
    frase2 = frase[: : -1]
    resultado = ""

    if frase == frase2:
        resultado = frase
        return resultado
    else:
        return resultado    
