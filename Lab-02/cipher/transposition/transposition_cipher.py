class TranspositionCipher:
    def encrypt_text(self, text, key):
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    def decrypt_text(self, text, key):
        num_of_columns = int(len(text) / key)
        num_of_rows = key
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)
        plaintext = [''] * num_of_columns
        col = 0
        row = 0
        for symbol in text:
            plaintext[col] += symbol
            col += 1
            if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
                col = 0
                row += 1
        return ''.join(plaintext)