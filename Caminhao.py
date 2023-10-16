import Veiculo
class Caminhao ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoCaminhao ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Caminhao")
        self.potencia = potencia
        self.tipoCaminhao = tipoCaminhao
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0

CaminhaoNovo = Caminhao('8885RTHF01Z12A76543098', 'SCANIA', 'Baú', '2010', 2.0, 'BONGO')
print(CaminhaoNovo.get_tipo())
print(CaminhaoNovo.potencia)
print(CaminhaoNovo.tipoCaminhao)
print(CaminhaoNovo.ligar())
