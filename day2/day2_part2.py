with open('input.txt', 'r') as arquivo:
    linhas = arquivo.readlines()


class CubeSet:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return str((self.r,self.g,self.b))
    def __repr__(self):
        return str((self.r, self.g, self.b))
    def subSet(self, outro):
        return (self.r <= outro.r and self.g <= outro.g and self.b <= outro.b)
    def max(self, outro):
        self.r = max(self.r, outro.r)
        self.g = max(self.g, outro.g)
        self.b = max(self.b, outro.b)
    def power(self):
        return self.r * self.g * self.b

def partes(set):
    colors = ['red', 'green', 'blue']
    values = [0, 0, 0]
    for token in set.split(','):
        for i, color in enumerate(colors):
            if color in token:
                values[i] += int(token.split()[0])

    return CubeSet(*values)



def main(linhas):
    p1 = CubeSet(12,13,14)
    soma = 0
    resultado_final = 0
    for num_jogo, i in enumerate(linhas):
        _,sem_jogo = i.split(':')
        num_jogo += 1
        sets = []
        for a in sem_jogo.split(';'):
            sets.append(partes(a))
        if all(s.subSet(p1) for s in sets):
            soma += num_jogo

        maximo = CubeSet(0,0,0)
        for s in sets:
            maximo.max(s)
        resultado_final += maximo.power()
    print(resultado_final)







main(linhas)