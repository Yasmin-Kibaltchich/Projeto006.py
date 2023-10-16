import Veiculo
class Kombi ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoKombi ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Kombi")
        self.potencia = potencia
        self.tipoKombi = tipoKombi
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0

Kombi = Kombi('8885AZKG01Z12A33921312', 'Wolksvagen', 'Pick Up', '2009', 2.0, 'Furgão')
print(Kombi.get_tipo())
print(Kombi.potencia)
print(Kombi.tipoKombi)
print(Kombi.ligar())
