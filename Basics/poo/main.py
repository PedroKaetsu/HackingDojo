from veiculo import Veiculo
from carro import Carro

celta = Veiculo('Vermelho', 4, 'GM', 20)

print(celta.cor)
print(celta.tanque)
celta.abastecer(40)
print(celta.tanque)

monza = Carro('Preto', 'GM', 30)

print(monza.rodas)
print(monza.tanque)
monza.abastecer(33)
print(monza.tanque)
