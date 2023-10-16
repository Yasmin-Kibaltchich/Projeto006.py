import Veiculo
class Motocicleta( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, cilindrada, numero_rodas, TipoMoto):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Motocicleta")
        self.cilindrada = cilindrada
        self.numero_rodas = numero_rodas
        self.TipoMoto = TipoMoto
        self.marcha = 1
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 1

Moto = Motocicleta('5AZKG01Z12A339037', 'Honda', 'VT', '2015', 600, 2, 'Custon')
print(Moto.get_tipo())
print(Moto.numero_rodas)
print(Moto.marca)
print(Moto.ligar())
