import socket
import threading
import json
import base64
from crypto_utils import *

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

session_key = b"1234567890123456"


def receive_messages():
    while True:
        try:
            raw = client.recv(4096)

            if not raw:
                break

            data = json.loads(raw.decode())

            iv = base64.b64decode(data["iv"])
            ciphertext = base64.b64decode(data["message"])
            received_hmac = base64.b64decode(data["hmac"])

            if verify_hmac(session_key, ciphertext, received_hmac):
                msg = aes_decrypt(session_key, iv, ciphertext)
                print(f"\nMensagem recebida: {msg}")
            else:
                print("\n⚠️ Mensagem adulterada recebida!")

        except Exception as e:
            print("Erro:", e)
            break


threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input("Você: ")

    iv, ciphertext = aes_encrypt(session_key, msg)

    print("\nMensagem criptografada enviada:")
    print(ciphertext)

    msg_hmac = generate_hmac(session_key, ciphertext)

    print("\nHMAC gerado:")
    print(msg_hmac)

    payload = {
        "iv": base64.b64encode(iv).decode(),
        "message": base64.b64encode(ciphertext).decode(),
        "hmac": base64.b64encode(msg_hmac).decode()
    }

    client.sendall(json.dumps(payload).encode())