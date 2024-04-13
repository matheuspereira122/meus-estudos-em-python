import conta
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):  # Corrected method name to 'idade'
        self._idade = idade
    
    
    def __repr__(self):
        class_name=type(self).__name__
        attr=(f'{self.nome!r},{self.idade!r}')
        return (f'{class_name}{attr}')
    
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int,):
        super().__init__(nome, idade)
        self.conta: conta.Conta|None=None


c1=Cliente('luiz',30)
c1.conta=conta.Contacorrente(111,222,0,0)
print(c1)
print(c1.conta)
c2=Cliente('luisa',20)
c2.conta=conta.Contacorrente(131,622,100,100)
print(c2)
print(c2.conta)