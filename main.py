"""
Diffie-Hellman key exchange
"""


class DH_Endpoint:
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


if __name__ == "__main__":
    message = "She eyes me like a Pisces when I am weak"
    my_public_key = 197
    my_private_key = 199
    your_public_key = 151
    your_private_key = 157

    me = DH_Endpoint(my_public_key, your_public_key, my_private_key)
    you = DH_Endpoint(my_public_key, your_public_key, your_private_key)

    my_partial_key = me.generate_partial_key()
    print(my_partial_key)

    your_partial_key = you.generate_partial_key()
    print(your_partial_key)

    my_full_key = me.generate_full_key(your_partial_key)
    print(my_full_key)

    your_full_key = you.generate_full_key(my_partial_key)
    print(your_full_key)

    your_encrypted_message = you.encrypt_message(message)
    print(your_encrypted_message)

    your_decrypted_message = me.decrypt_message(your_encrypted_message)
    print(your_decrypted_message)

