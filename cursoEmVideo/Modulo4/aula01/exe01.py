class Gafanhoto:
    def __init__(self, nome, idade, sexo, login):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.login = login
        self.totalAssistido = 0

    def assistirMaisUm(self):
        self.totalAssistido += 1    
    def __str__(self):
        return f'Gafanhoto: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Login: {self.login}, Total Assistido: {self.totalAssistido}'
g1 = Gafanhoto('João', 20, 'M', 'joaogamer')
g1.assistirMaisUm()
g1.assistirMaisUm()
g1.assistirMaisUm()
print(g1)