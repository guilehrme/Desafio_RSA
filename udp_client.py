import random
import socket
from Crypto.Util import number

# Função para gerar um número primo
def gerarNumeroPrimo():
    p = number.getPrime(4096)
    return p

# Função para descriptografar um número usando o algoritmo RSA
def descriptografar(letraDescriptografada, d, N):
    letraDescriptografada = pow(letraDescriptografada, d, N)
    return letraDescriptografada

# Geração de números primos e cálculo de chaves pública e privada
q = gerarNumeroPrimo()
p = gerarNumeroPrimo()
N = p * q
totienteN = p * q - p - q + 1
e = gerarNumeroPrimo()

while e > totienteN:
    e = gerarNumeroPrimo()

while totienteN % e == 0:
    while e > totienteN:
        e = gerarNumeroPrimo()

d = pow(e, -1, totienteN)

ChavePublica = ""
msgDoCliente = str(e) + '-' + str(N)
bytesParaEnviar = str.encode(msgDoCliente)
#Endereço de IP da do Usuário:
enderecoLocal = "192.168.15.64"
#==================================================================================================
enderecoServidorPorta = (enderecoLocal, 20001)
tamanhoBuffer = 250000
encerrarConexao = False

# Criação de um socket UDP e envio da chave pública ao servidor
SocketClienteUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
SocketClienteUDP.sendto(bytesParaEnviar, enderecoServidorPorta)

letras = []
msgDoServidor = ''

# Recebe as letras criptografadas do servidor até receber a mensagem "Fim"
while msgDoServidor != 'Fim':
    msgDoServidor = SocketClienteUDP.recvfrom(tamanhoBuffer)
    msgDoServidor = str(msgDoServidor[0], "utf-8")

    if msgDoServidor != 'Fim':
        letras.append(msgDoServidor)

textoDescriptografado = ''

# Descriptografa cada letra e forma a mensagem original
for letraCriptografada in letras:
    letraCriptografadaInt = int(letraCriptografada)
    numeroOriginal = descriptografar(letraCriptografadaInt, d, N)
    letraOriginal = chr(numeroOriginal)
    textoDescriptografado = textoDescriptografado + str(letraOriginal)

print(f'Mensagem descriptografada recebida do servidor: {textoDescriptografado}')
