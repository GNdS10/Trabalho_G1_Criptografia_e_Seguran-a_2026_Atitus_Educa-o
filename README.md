# Sistema de Chat Seguro

Trabalho da disciplina de ** Criptografia e Segurança**

## 
Gabriel Nogueira dos Santos 
RA:1127692

---

## Descrição

O projeto consiste em um sistema de chat em rede no modelo cliente-servidor.

As mensagens enviadas entre os clientes são criptografadas utilizando **AES-128**, onde, garante a confidencialidade dos dados.

Também foi utilizado **HMAC com SHA-256** para verificar a integridade das mensagens, que permite detectar alterações durante a transmissão.

---

## Algoritmos utilizados

- **AES-128** → criptografia das mensagens
- **HMAC SHA-256** → integridade das mensagens

---

## Instalação

```bash
pip install cryptography
```

---

## Execução

### Servidor

```bash
python server.py
```

### Clientes

```bash
python client.py
```
```bash
python client.py
```
Executar em dois terminais para testar a troca de mensagens.

---

## Arquivos do projeto

- `server.py` → servidor do chat
- `client.py` → cliente do chat
- `crypto_utils.py` → funções de criptografia



---

## Relatório Técnico

O projeto foi desenvolvido no modelo **cliente-servidor**, onde um servidor central fica responsável por receber as conexões dos clientes e encaminhar as mensagens entre eles.

A linguagem escolhida foi **Python**, por ser mais prática para desenvolver a comunicação em rede usando sockets e por possuir bibliotecas prontas para a parte de criptografia.

Para proteger o conteúdo das mensagens, foi utilizado o algoritmo **AES-128**, que faz a criptografia antes do envio, evitando que a mensagem trafegue em texto puro pela rede.

Além disso, foi utilizado **HMAC com SHA-256** para verificar a integridade das mensagens. Com isso, caso alguma informação seja alterada durante a transmissão, o sistema consegue identificar e rejeitar a mensagem.

O sistema também permite que mais de um cliente se conecte ao servidor ao mesmo tempo, possibilitando a troca de mensagens em tempo real.

Com isso, o projeto garante principalmente:

- **confidencialidade**, pois a mensagem é criptografada
- **integridade**, pois alterações são detectadas pelo HMAC
- **comunicação em rede segura**, com múltiplos clientes conectados
