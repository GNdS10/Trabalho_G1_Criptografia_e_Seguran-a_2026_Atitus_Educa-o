import socket
import threading
import json
import base64
from crypto_utils import *

HOST = "0.0.0.0"
PORT = 5000

clients = []

# chave AES fixa de 128 bits
chat_key = b"1234567890123456"


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.sendall(message)
            except:
                pass


def handle_client(conn, addr):
    print(f"Cliente conectado: {addr}")

    clients.append(conn)

    while True:
        try:
            raw = conn.recv(4096)

            print("\n==============================")
            print("PACOTE BRUTO RECEBIDO:")
            print(raw)
            print("==============================\n")

            if not raw:
                break

            data = json.loads(raw.decode())

            iv = base64.b64decode(data["iv"])
            ciphertext = base64.b64decode(data["message"])
            received_hmac = base64.b64decode(data["hmac"])

            print("Mensagem criptografada (AES):")
            print(ciphertext)

            print("\nHMAC recebido:")
            print(received_hmac)

            if not verify_hmac(chat_key, ciphertext, received_hmac):
                print("\n⚠️ Mensagem adulterada detectada!")
                continue

            msg = aes_decrypt(chat_key, iv, ciphertext)

            print(f"\nMensagem descriptografada: {msg}")

            broadcast(raw, conn)

        except Exception as e:
            print("Erro:", e)
            break

    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Servidor rodando em {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )

        thread.start()


if __name__ == "__main__":
    start_server()