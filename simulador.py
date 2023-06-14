'''
Simulador de Renda Fixa baseada na taxa de juros atual do Brasil, ou seja, baseando-se na
taxa Selic.
'''

cabecario = 'Simulador de Renda Fixa - CDB\n'
observacao = '''

Obs.: A simulação é feita com base na taxa Básica de Juros(Selic)
onde é calculada o valor do montante com base no investimento inicial 
e o tempo em que esse valor está no CDB, etc...
_____________________________________________________________________

      "Lembrando que o tempo deve ser informado em meses"

'''
divisaoText = '='

print(cabecario + divisaoText * len(cabecario) + observacao + divisaoText * len(cabecario))

class Simular:
    def __init__(self, CDI, taxaBasica, valorInicial, tempoMeses):
        self.cdi = CDI
        self.taxa = taxaBasica
        self.valor = valorInicial
        self.tempo = tempoMeses

    def getData(self):
        taxaCalc = float(self.taxa)/100
        cdiCalc = taxaCalc * 99/100
        montante = float(self.valor) * (1 + cdiCalc/12)**(int(self.tempo)*12)
        resultado = f'O montante é: R${montante: _.2f}'
        resultado = resultado.replace('.',',').replace('_','.')
        return resultado

'''
cdi = input('Digite a oferta do CDI: \n')
valorInv = input('Digite o valor investido:\n')
taxaJuros = input('Digite a taxa de juros:\n')
tempoM = input('Digite o tempo investido:\n')
'''

def valor_inteiro(message):
    while True:
        try:
            valor = int(input(message))
            return valor
        except ValueError:
            print('Erro: Digite um valor válido. Ex: 10, 20, 100, etc...\n')

def valor_float(message):
    while True:
        try:
            valor = float(input(message))
            return valor
        except ValueError:
            print('Erro: Digite um valor válido. Ex: 100.55\n')

def limites_validos(value, valor_minimo):
    if value < valor_minimo:
        raise ValueError(f'Digite um valor acima de {valor_minimo}')

cdi = valor_inteiro('Digite o CDI ofertado:\n')
valorInv = valor_float('Digite o seu investimento inicial:\n')
taxaJuros = valor_float('Digite a taxa Selic Atual:\n')
tempoM = valor_inteiro('Digite quantos meses pretende deixar investido:\n')

try:
    limites_validos(cdi, 0)
    limites_validos(valorInv, 100)
    limites_validos(taxaJuros, 1)
    limites_validos(tempoM, 1)
    
    simulando = Simular(cdi, taxaJuros, valorInv, tempoM)
    result = simulando.getData()
    print(result)

except ValueError as err:
    print(err)