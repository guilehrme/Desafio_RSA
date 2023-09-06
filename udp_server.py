import socket

# Configuração das variáveis do servidor
#==================================================================================================
#Endereço de IP da do Usuário:
enderecoLocal = "192.168.15.64"
#==================================================================================================
portaLocal = 20001
tamanhoBuffer = 250000
chavePublica = ''
listaVariaveis = []
textoCriptografia = ''
msg = "The information security is of significant importance to ensure the privacy of communications"
msgDoServidor = ''

# Função para criptografar um número usando o algoritmo RSA
def criptografar(numero, e, N):
    letraCriptografada = pow(numero, e, N)
    return letraCriptografada

# Criação de um socket UDP e vinculação ao endereço e porta
SocketServidorUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
SocketServidorUDP.bind((enderecoLocal, portaLocal))
print("Servidor UDP ativo e ouvindo")

# Loop principal do servidor
while True:
    bytesEnderecoPar = SocketServidorUDP.recvfrom(tamanhoBuffer)
    mensagem = bytesEnderecoPar[0]
    endereco = bytesEnderecoPar[1]

    print(f"Mensagem recebida de {endereco}: {mensagem}")

    # Se a chave pública ainda não foi definida, a primeira mensagem é tratada como a chave pública
    if chavePublica == '':
        chavePublica = mensagem

    listaVariaveis = str(chavePublica).split('-')
    e, N = listaVariaveis
    e = e.replace("b'", "")
    N = N.replace("'", "")
    eInt = int(e)
    NInt = int(N)

    # Criptografa cada caractere da mensagem de exemplo e envia de volta ao cliente
    for letra in msg:
        numero = ord(letra)
        criptografia = criptografar(numero, eInt, NInt)
        bytesParaEnviar = str.encode(str(criptografia))
        SocketServidorUDP.sendto(bytesParaEnviar, endereco)

    msgDoServidor = textoCriptografia

    mensagemCliente = str(mensagem, "utf-8")
    enderecoCliente = "Endereço IP do Cliente:{}".format(endereco)

    # Envia a mensagem "Fim" para indicar o término da transmissão
    bytesParaEnviar = str.encode("Fim")
    SocketServidorUDP.sendto(bytesParaEnviar, endereco)
    print(f"Mensagem 'Fim' enviada para {endereco}")