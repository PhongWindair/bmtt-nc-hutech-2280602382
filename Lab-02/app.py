from flask import Flask, render_template, request, redirect, url_for
from cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()

@app.route('/')
def index():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plain_text = request.form['plain_text']
    key = int(request.form['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return render_template('caesar.html', plain_text=plain_text, key=key, result=encrypted_text, action='encrypt')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    cipher_text = request.form['cipher_text']
    key = int(request.form['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return render_template('caesar.html', cipher_text=cipher_text, key=key, result=decrypted_text, action='decrypt')

if __name__ == '__main__':
    app.run(debug=True)