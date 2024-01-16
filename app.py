class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
pessoa = Pessoa(nome = "Max", idade = 23)

print(pessoa.nome)
print(pessoa.idade)