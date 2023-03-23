def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

# print('Insira o valor a ser convertido')
# entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
# valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
# print(valorConvertido)




def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def byteparakilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    bytesCalculado = valorASerConvertido / 1024
    return bytesCalculado

def kilobyteparabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para byte')
    kilobyteCalculado = valorASerConvertido * 1024
    return kilobyteCalculado

# print('Insira o valor a ser convertido')
# entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
# valorConvertido = kilobyteparabyte(entradaDoTecladoValorASerConvertido)
# print(valorConvertido)







def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def megabyteparakilobyte(valorASerConvertido):
    print('Valor convertido de megabyte para kilobyte')
    megabytesCalculado = valorASerConvertido / 1024
    return megabytesCalculado

def kilobyteparamegabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para megabyte')
    kilobyteCalculado = valorASerConvertido * 1024
    return kilobyteCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = kilobyteparamegabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

