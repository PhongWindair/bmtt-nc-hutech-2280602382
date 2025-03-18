class VigenereCipher:
    def __init__(self, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.alphabet = alphabet

    def encrypt_text(self, text, key):
        key = key.upper()
        text = text.upper()
        encrypted_text = []
        key_index = 0

        for char in text:
            if char in self.alphabet:
                text_index = self.alphabet.index(char)
                key_char = key[key_index % len(key)]
                key_index += 1
                key_index_value = self.alphabet.index(key_char)
                encrypted_char = self.alphabet[(text_index + key_index_value) % len(self.alphabet)]
                encrypted_text.append(encrypted_char)
            else:
                encrypted_text.append(char)

        return ''.join(encrypted_text)

    def decrypt_text(self, text, key):
        key = key.upper()
        text = text.upper()
        decrypted_text = []
        key_index = 0

        for char in text:
            if char in self.alphabet:
                text_index = self.alphabet.index(char)
                key_char = key[key_index % len(key)]
                key_index += 1
                key_index_value = self.alphabet.index(key_char)
                decrypted_char = self.alphabet[(text_index - key_index_value) % len(self.alphabet)]
                decrypted_text.append(decrypted_char)
            else:
                decrypted_text.append(char)

        return ''.join(decrypted_text)