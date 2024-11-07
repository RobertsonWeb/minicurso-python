class Funcionario():
    nome = None
    departamento = None

    def imprimir_cracha(self):
        print(20*'=')
        print(self.nome.upper())
        print(self.departamento.upper())
        print(20*'=')