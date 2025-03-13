class PlayfairCipher:
    def __init__(self, key):
        # Prepare the key and grid
        self.key = self.prepare_key(key)
        self.grid = self.create_grid(self.key)

    def prepare_key(self, key):
        # Remove duplicates and make it upper case
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
        key = key.replace("J", "I")  # Consider J as I for simplicity
        return key.upper()

    def create_grid(self, key):
        # Create the 5x5 grid with the key and the remaining letters of the alphabet
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note that J is excluded
        grid = list(key)
        
        for letter in alphabet:
            if letter not in grid:
                grid.append(letter)

        return [grid[i:i + 5] for i in range(0, len(grid), 5)]

    def display_grid(self):
        # Print the 5x5 grid
        for row in self.grid:
            print(' '.join(row))

    def prepare_text(self, text):
        # Prepare the text by removing non-alphabetic characters and splitting into digraphs
        text = text.upper().replace("J", "I").replace(" ", "")
        
        # Add an 'X' if two same letters appear together
        prepared_text = []
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                prepared_text.append(text[i] + 'X')
                i += 1
            else:
                prepared_text.append(text[i:i+2] if i + 1 < len(text) else text[i] + 'X')
                i += 2
        return prepared_text

    def find_position(self, letter):
        # Find the row and column of the letter in the grid
        for r in range(5):
            for c in range(5):
                if self.grid[r][c] == letter:
                    return r, c
        return None

    def encrypt_pair(self, pair):
        r1, c1 = self.find_position(pair[0])
        r2, c2 = self.find_position(pair[1])

        if r1 == r2:
            # Same row: move to the right
            c1, c2 = (c1 + 1) % 5, (c2 + 1) % 5
        elif c1 == c2:
            # Same column: move down
            r1, r2 = (r1 + 1) % 5, (r2 + 1) % 5
        else:
            # Rectangle: swap columns
            c1, c2 = c2, c1

        return self.grid[r1][c1] + self.grid[r2][c2]

    def decrypt_pair(self, pair):
        r1, c1 = self.find_position(pair[0])
        r2, c2 = self.find_position(pair[1])

        if r1 == r2:
            # Same row: move to the left
            c1, c2 = (c1 - 1) % 5, (c2 - 1) % 5
        elif c1 == c2:
            # Same column: move up
            r1, r2 = (r1 - 1) % 5, (r2 - 1) % 5
        else:
            # Rectangle: swap columns
            c1, c2 = c2, c1

        return self.grid[r1][c1] + self.grid[r2][c2]

    def encrypt(self, text):
        # Prepare the text and encrypt each pair
        prepared_text = self.prepare_text(text)
        cipher_text = ''.join(self.encrypt_pair(pair) for pair in prepared_text)
        return cipher_text

    def decrypt(self, text):
        # Decrypt each pair and return the result
        prepared_text = [text[i:i + 2] for i in range(0, len(text), 2)]
        plain_text = ''.join(self.decrypt_pair(pair) for pair in prepared_text)
        return plain_text

