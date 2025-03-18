from flask import Flask, jsonify, request
from cipher.rsa import RSACipher
import rsa
app = Flask(__name__)

rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    public_key = rsa.PublicKey.load_pkcs1(key.encode('utf-8'))
    encrypted_text = rsa_cipher.encrypt(plain_text, public_key)
    return jsonify({'encrypted_message': encrypted_text.hex()})

@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    private_key = rsa.PrivateKey.load_pkcs1(key.encode('utf-8'))
    decrypted_text = rsa_cipher.decrypt(bytes.fromhex(cipher_text), private_key)
    return jsonify({'decrypted_message': decrypted_text})

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign():
    data = request.json
    message = data['message']
    key = data['key']
    private_key = rsa.PrivateKey.load_pkcs1(key.encode('utf-8'))
    signature = rsa_cipher.sign(message, private_key)
    return jsonify({'signature': signature.hex()})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify():
    data = request.json
    message = data['message']
    signature = data['signature']
    key = data['key']
    public_key = rsa.PublicKey.load_pkcs1(key.encode('utf-8'))
    verified = rsa_cipher.verify(message, bytes.fromhex(signature), public_key)
    return jsonify({'verified': verified})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)