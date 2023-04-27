listasdeunidades = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]

def convert(quantidade, unidadeone, unidadetwo):
    fator = 1
    if unidadeone == "bit":
        fator /=8
        unidadeone = "byte"
    indiceinicial = listasdeunidades.index(unidadeone)
    indicefinal = listasdeunidades.index(unidadetwo)
    if indiceinicial < indicefinal:
        for i in range(indiceinicial + 1, indicefinal + 1):
            fator /= 1024
    else:
        for i in range(indicefinal + 1, indiceinicial + 1):
            fator *= 1024
        if unidadetwo == "bit":
            fator = (fator/1024)*8
    
    quantidadedestino = quantidade * fator
    
    return quantidadedestino


quantidade = float(input("Digite a quantidade a ser convertida: "))
unidade_one = input("Digite a unidade de medida inicial: ")
unidade_two = input("Digite a unidade de medida final: ")


quantidade_convertida = convert(quantidade, unidade_one, unidade_two)
print(f"{quantidade} {unidade_one} = {quantidade_convertida} {unidade_two}")
    
                       
  