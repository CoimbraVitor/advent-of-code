with open('input.txt', "r") as arquivo:
   linha = arquivo.readlines()


primeiro = None
ultimo = None
lista = []

for a in linha:
    a.split(',')
    for i in a:
        if i.isdigit():
            if primeiro is None:
                primeiro = i
            ultimo = i
    sominha = primeiro + ultimo
    lista.append(int(sominha))
    primeiro = None


print(sum(lista))