class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Create a list of lists to represent the rails
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1 means downward, -1 means upward

        # Place characters in the rails in a zigzag pattern
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1  # Move downward
            elif rail_index == num_rails - 1:
                direction = -1  # Move upward
            rail_index += direction

        # Join all the rails together to form the cipher text
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Create a list to track the lengths of each rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Calculate the number of characters in each rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Split the cipher text into the respective rails
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start+length]))
            start += length

        # Decrypt by reading characters from the rails in a zigzag pattern
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1  # Move downward
            elif rail_index == num_rails - 1:
                direction = -1  # Move upward
            rail_index += direction

        return plain_text
