from flask import Flask, request, jsonify
from cipher.railfence import RailFenceCipher
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.Transposition import TranspositionCipher

app = Flask(__name__)

# Instantiate cipher objects
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
transpositon_cipher = TranspositionCipher()

# Caesar Cipher routes
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Vigenère Cipher routes
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    encrypt_text = vigenere_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():  # Fixed function name here
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# RailFence Cipher routes
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypt_text = railfence_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypt_text = railfence_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypt_text})

# Transposition Cipher routes
@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypt_text = transpositon_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypt_text = transpositon_cipher.decrypt(cipher_text, key)  # Fixed to use transposition_cipher
    return jsonify({'decrypted_message': decrypt_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
