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
