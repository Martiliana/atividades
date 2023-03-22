"""
Faça um Programa que mostre a mensagem "Alo mundo" na tela.

Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

Faça um Programa que peça dois números e imprima a soma.

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

Faça um Programa que converta metros para centímetros.

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

C = 5 * ((F-32) / 9).

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o produto do dobro do primeiro com metade do segundo .

a soma do triplo do primeiro com o terceiro.

o terceiro elevado ao cubo.

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58

Para mulheres: (62.1*h) - 44.7

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.

quanto pagou ao INSS.

quanto pagou ao sindicato.

o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$

- IR (11%) : R$

- INSS (8%) : R$

- Sindicato ( 5%) : R$

= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.



Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;

comprar apenas galões de 3,6 litros;

misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).



"""
"""
import math

print("9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.\n"
      "C = 5 * ((F-32) / 9).\n")

temp_f = float(input("digite a temperatura em Fahrenheit: "))
temp_c = round((5 * ((temp_f-32) / 9)),1)

print(f"A temperatura de {temp_f} Fº é igual a {temp_c} Cº")


print("\n13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,\n"
      "utilizando as seguintes fórmulas:\n"
      "Para homens: (72.7*altura) - 58\n"
      "Para mulheres: (62.1*altura) - 44.7\n")

altura = float(input("Digite a sua altura: "))

homen = (72.7*altura) - 58
mulher = (62.1*altura) - 44.7

pergunta = input("Voce quer calcular para homen ou mulher?H/M: ").upper()
print(pergunta)

if pergunta[0] == "H":
    print(f'O peso ideal para o homen é {homen:.1f}')
else:
    print(f'O peso ideal para a mulher é {mulher:.1f}')
"""

"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável 
multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 


peso = float(input("Quantos kg voce pescou? "))

if peso > 50:
    multa = (peso - 50)*4
    print(f"Voce foi multado em R${multa}")
else:
    print("Voce nao excedeu o limite de 50kg")
"""

"""
+
-
*
/
//
**
%
"""
"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 


area = float(input("Digite quantos metros quadrados voce vai pintar: "))

lata = 18*3

quantidade_latas = math.ceil(area/lata)

print(f"Voce ira gastar {quantidade_latas}, o preco total e R${quantidade_latas*80}")

"""

"""
 
17-Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. 

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 

comprar apenas latas de 18 litros; 

comprar apenas galões de 3,6 litros; 

misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.



area = float(input('Digite quantos metros você quer pintar'))
print(area%108)
print(area/108)
lata =  18*6 #108 metros quadrados
galao = 3*6*6 #21.6 metros quadrados

apenas_latas = math.ceil(area/lata)
apenas_galao = math.ceil(area/galao)

print(f'Você precisara apenas de {apenas_latas}lata (s) R$= {apenas_latas*80}')
print(f'voce precisara apenas de {apenas_galao} galão (es) = R$ {apenas_galao*25}')

margem_area = area*1.1


latas_misturadas = math.ceil(margem_area/108)

galao_misturadas = math.ceil(margem_area/21.6)

if margem_area <= 64.8:
    print(galao_misturadas,'galão (s)')

elif (margem_area > 64.8) and margem_area <= 108:
        print('1 lata')
else:
    if margem_area % 108 < 60:
            galao_total = math.ceil(margem_area%108/galao)
            print(f'Você vai gastar {margem_area/lata} latas  e {galao_total} galao')
    else:
        print(f'Voce vai gastar {latas_misturadas}lata')
"""










