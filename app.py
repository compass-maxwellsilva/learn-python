nomes = "Maxwell"
print(nomes)

class Pessoa:
    def _init_(self, nome, idade):
        self.name = nome
        self.age = idade
pessoa = Pessoa("Max", 23)

print(pessoa.name)
print(pessoa.age)