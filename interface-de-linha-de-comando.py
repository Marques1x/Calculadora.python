from calculadora import converterStringParaFloat, bitParaByte, byteParaBit, byteparakilobyte, kilobyteparabyte, megabyteparakilobyte, kilobyteparamegabyte, megabyteparagigabyte, gigabyteparamegabyte, terabyteparagigabyte, gigabyteparaterabyte, terabyteparapetabyte, petabyteparaterabyte
print('-Escreva 1 para bitParaByte \n  -Escreva 2 para byteParaBit \n  -Escreva 3 para byteparakilobyte \n  -Escreva 4 para kilobyteparabyte \n  -Escreva 5 para megabyteparakilobyte   \n  -Escreva 6 para kilobyteparamegabyte   \n  -Escreva 7 para megabyteparagigabyte   \n  -Escreva 8  para gigabyteparamegabyte  \n  -Escreva 9 para terabyteparagigabyte   \n  -Escreva 10 para gigabyteparaterabyte  \n  -Escreva 11 para terabyteparapetabyte  \n  -Escreva 12 para petabyteparaterabyte' )
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)




elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





    
elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteparakilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido =  kilobyteparabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = megabyteparakilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = kilobyteparamegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '7'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = megabyteparagigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '8'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = gigabyteparamegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '9'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = terabyteparagigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '10'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = gigabyteparaterabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)







elif(funcEscolha == '11'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = terabyteparapetabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)





elif(funcEscolha == '12'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = petabyteparaterabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)


else:
    print('errou')