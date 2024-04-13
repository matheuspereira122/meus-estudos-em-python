import abc
class Conta(abc.ABC):
    def __init__(self,agencia,conta, saldo):
        self.agencia=agencia
        self.conta=conta
        self.saldo=saldo
    @abc.abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')
    
    def __repr__(self):
        class_name=type(self).__name__
        attr=(f'{self.agencia!r},{self.conta!r},{self.saldo}')
        return (f'{class_name}, {attr}')
    
class Contapoupanca(Conta):
     def sacar(self,valor):
        valor_pos_sacar=self.saldo-valor
        if valor_pos_sacar>=0:
            self.saldo-=valor
            self.datalhes=(f'sacando {valor}')
            return self.saldo
        print('não foi posivel sacar nao tem dinheiro na conta')
        self.datalhes=(f'saque negado {valor}')
class Contacorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    def __repr__(self):
        class_name=type(self).__name__
        attr=(f'Agencia:{self.agencia!r},N°conta:{self.conta!r},Saldo:{self.saldo},Limite:{self.limite}')
        return (f'{class_name}, {attr}')
    
     
    
    def sacar(self,valor):
        limite_maximo = -self.limite
    
    
    

        valor_pos_sacar=self.saldo-valor
        
            
        if valor_pos_sacar>=0:

                self.saldo-=valor
                self.datalhes=(f'sacando {valor}')
                return self.saldo
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
    
cp1 = Contapoupanca(111, 222,5)
cp1.sacar(1)
cp1.depositar(1)
cp1.sacar(1)
cp1.sacar(1)
print('##')
cc1 = Contacorrente(111, 222, 0, 100)
cc1.sacar(1)
cc1.depositar(1)
cc1.sacar(1)
cc1.sacar(1)
cc1.sacar(98)
cc1.sacar(1)
print('##')
