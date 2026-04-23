# Sistema de Chat Seguro

Trabalho da disciplina - Criptografia e Segurança

Aluno: Gabriel Nogueira dos Santos



## Descrição

O projeto consiste em um sistema de chat em rede no modelo cliente-servidor.

As mensagens enviadas entre os clientes são criptografadas utilizando **AES-128**, que garante a cofindencialidade dos dados

Também foi utilizado **HMAC com SHA-256** para verificar a integridade das mensagens,  que permite detectar se houve alterações durante a transmissão.



## Algoritmos utilizados

- **AES-128** → criptografia das mensagens
- **HMAC SHA-256** → integridade das mensagens



## Instalação

CMD
pip install cryptography
```


### Servidor

CMD
python server.py


### Clientes

CMD
python client.py


Executar em dois terminais para testar a troca de mensagens.



## Arquivos do projeto

- `server.py` → servidor do chat
- `client.py` → cliente do chat
- `crypto_utils.py` → funções de criptografia
