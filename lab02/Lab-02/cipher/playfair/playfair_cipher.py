class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.matrix = self.generate_matrix(key)

    def generate_matrix(self, key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key = "".join(sorted(set(key.upper()), key=lambda x: key.index(x)))
        key = key.replace("J", "I")
        matrix = []
        for char in key:
            if char not in matrix:
                matrix.append(char)
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def preprocess_text(self, text):
        text = text.upper().replace("J", "I")
        processed_text = ""
        i = 0
        while i < len(text):
            processed_text += text[i]
            if i + 1 < len(text) and text[i] == text[i + 1]:
                processed_text += "X"
            elif i + 1 < len(text):
                processed_text += text[i + 1]
                i += 1
            i += 1
        if len(processed_text) % 2 != 0:
            processed_text += "X"
        return processed_text

    def find_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == char:
                    return row, col
        return None, None

    def encrypt_pair(self, a, b):
        row_a, col_a = self.find_position(a)
        row_b, col_b = self.find_position(b)
        if row_a is None or row_b is None:
            raise ValueError(f"Character {a} or {b} not found in matrix")
        if row_a == row_b:
            return self.matrix[row_a][(col_a + 1) % 5] + self.matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            return self.matrix[(row_a + 1) % 5][col_a] + self.matrix[(row_b + 1) % 5][col_b]
        else:
            return self.matrix[row_a][col_b] + self.matrix[row_b][col_a]

    def decrypt_pair(self, a, b):
        row_a, col_a = self.find_position(a)
        row_b, col_b = self.find_position(b)
        if row_a is None or row_b is None:
            raise ValueError(f"Character {a} or {b} not found in matrix")
        if row_a == row_b:
            return self.matrix[row_a][(col_a - 1) % 5] + self.matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            return self.matrix[(row_a - 1) % 5][col_a] + self.matrix[(row_b - 1) % 5][col_b]
        else:
            return self.matrix[row_a][col_b] + self.matrix[row_b][col_a]

    def encrypt_text(self, text):
        text = self.preprocess_text(text)
        encrypted_text = ""
        for i in range(0, len(text), 2):
            encrypted_text += self.encrypt_pair(text[i], text[i + 1])
        return encrypted_text

    def decrypt_text(self, text):
        decrypted_text = ""
        for i in range(0, len(text), 2):
            decrypted_text += self.decrypt_pair(text[i], text[i + 1])
        return decrypted_text

    def create_matrix(self):
        return self.matrix