# Desafio_RSA
Solução baseada no protocolo UDP que transmite uma mensagem criptografada com chave de 4096bits utilizando a criptografia RSA.

Para executar o código é necessário o uso de 2 bibliotecas: 
- 1° A biblioteca para utilizar o protocolo UDP a biblioteca socket => pip install sockets
- 2° A biblioteca que busca números primos de 4096 bits no python a biblioteca pycryptodome => pip install pycryptodome


*PROCESSO:*
- O cliente gera suas próprias chaves pública e privada.
- A chave pública é enviada ao servidor via UDP, que a usará para criptografar a mensagem.
- O servidor espera pela comunicação do cliente e recebe a chave pública do cliente quando ela chega.
- Usando a chave pública do cliente, o servidor criptografa uma mensagem de exemplo usando o algoritmo RSA.
- As letras criptografadas são enviadas de volta ao cliente, que as descriptografa e forma a mensagem original.
- A comunicação é encerrada com uma mensagem 'Fim' para indicar que a transmissão foi concluída.
