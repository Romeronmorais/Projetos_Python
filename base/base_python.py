# Python 
# App lista exemplificação dos conceitos básicos do Python

import os,time 

print('Programa simples mostra sintaxe do Python')
print('-----------------------------------------')

opcao = 4

while opcao != 0:     
    os.system('cls')

    print('Menu')
    print('1 - Soma dois números')
    print('2 - Cálculo do IMC')
    print('3 - Gerar sequência Fibonacci')    
    opcao = input('Digite a opção: ')      
    
    if opcao == '1':
        print('')        
        print('-------------------------------')
        print('1 - Soma dois números')    
        print('-------------------------------')
        print('')        
        numero1 = input('Digite o primeiro número: ')  
        numero2 = input('Digite o segundo número: ')
        resultado = int(numero1) + int(numero2)
        print('A soma dos dois numero: ' + str(resultado))
        time.sleep(10)  
    
    if opcao == '2':
        print('')        
        print('-------------------------------')
        print('2 - Cálculo do IMC')    
        print('-------------------------------')
        print('')        
        peso = input('Digite seu peso: ')  
        altura = input('Digite sua altura: ')
        resultado = float(peso) / (float(altura) * float(altura))

        # Tabela de IMC        
        if resultado < 17:
            print('IMC: ' + str(resultado) + ' Muito abaixo do peso')
        elif resultado >= 17 and resultado <= 18.49:
            print('IMC: ' + str(resultado) + ' Abaixo do peso')
        elif resultado >= 18.50 and resultado <= 24.99:
            print('IMC: ' + str(resultado) + ' Peso normal')
        elif resultado >= 25.00 and resultado <= 29.99:
            print('IMC: ' + str(resultado) + ' Acima do peso')                    
        elif resultado >= 30.00 and resultado <= 34.99:
            print('IMC: ' + str(resultado) + ' Obesidade I')  
        elif resultado >= 35.00 and resultado <= 39.99:
            print('IMC: ' + str(resultado) + ' Obesidade II (severa)')                         
        else: #  resultado > 50.00:
            print('IMC: ' + str(resultado) + ' Obesidade III (mórbida)') 

        time.sleep(10) 

    if opcao == '3':
        print('')        
        print('-------------------------------')
        print('3 - Gerar sequência Fibonacci')    
        print('-------------------------------')
        print('')        
        numero1 = input('Digite um número: ')          

        resultado      = int(numero1)
        aux            = 0
        primeiro       = 0
        ultimo         = 1
        resultadoFinal = []

        while aux < resultado:
            aux = primeiro + ultimo
            primeiro = ultimo
            ultimo = aux
            resultadoFinal.append(aux)

        print('Resultado fibonacci:')
        print(resultadoFinal)
        time.sleep(10)  