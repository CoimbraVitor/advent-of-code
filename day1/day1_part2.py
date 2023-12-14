with open('input.txt', "r") as arquivo:
   linhas = arquivo.readlines()

soma_total = 0
numeros = []
for linha in linhas:
    elementos = linha.split(',')
    sominha = []

    for elemento in elementos:
        elemento = elemento.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine')

        for i in elemento:
            if i.isdigit():
                sominha.append(i)

    if sominha:
        primeiro = str(sominha[0])
        ultimo = str(sominha[-1])
        resultado = int(primeiro + ultimo)
        numeros.append(resultado)

soma = sum(numeros)
print(soma)