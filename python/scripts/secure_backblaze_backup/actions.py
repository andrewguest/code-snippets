from cryptography.fernet import Fernet


def encrypt_file(file_to_encrypt, encryption_key):
    """Encrypt a file

    Args:
        file_to_encrypt (str): Name of file to encrypt.
        encryption_key (str): Encryption key to use to encrypt file.
    """

    f = Fernet(encryption_key)

    with open(file_to_encrypt, "rb") as file:
        file_data = file.read()  # read all file data
        encrypted_data = f.encrypt(file_data)  # encrypt data

        with open(file_to_encrypt, "wb") as file:  # write the encrypted data
            file.write(encrypted_data)


def decrypt_file(file_to_decrypt, decryption_key):
    """Decrypt a file

    Args:
        file_to_decrypt (str): Name of file to decrypt.
        decryption_key (str): Decryption key to use.
    """
    f = Fernet(decryption_key)

    with open(file_to_decrypt, "rb") as file:  # read the encrypted data
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)  # decrypt data

    with open(file_to_decrypt, "wb") as file:  # write the original file
        file.write(decrypted_data)
