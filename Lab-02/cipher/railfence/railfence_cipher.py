class RailFenceCipher:
    def __init__(self, num_rails):
        self.num_rails = num_rails

    def encrypt_text(self, text):
        rail = [''] * self.num_rails
        rail_direction = 1
        rail_index = 0

        for char in text:
            rail[rail_index] += char
            rail_index += rail_direction

            if rail_index == 0 or rail_index == self.num_rails - 1:
                rail_direction *= -1

        return ''.join(rail)

    def decrypt_text(self, text):
        rail = [''] * self.num_rails
        rail_length = [0] * self.num_rails
        rail_direction = 1
        rail_index = 0

        for char in text:
            rail_length[rail_index] += 1
            rail_index += rail_direction

            if rail_index == 0 or rail_index == self.num_rails - 1:
                rail_direction *= -1

        index = 0
        for i in range(self.num_rails):
            rail[i] = text[index:index + rail_length[i]]
            index += rail_length[i]

        decrypted_text = []
        rail_index = 0
        rail_direction = 1

        for i in range(len(text)):
            decrypted_text.append(rail[rail_index][0])
            rail[rail_index] = rail[rail_index][1:]
            rail_index += rail_direction

            if rail_index == 0 or rail_index == self.num_rails - 1:
                rail_direction *= -1

        return ''.join(decrypted_text)