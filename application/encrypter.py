import pyAesCrypt
from os import stat, remove

"""
-----------------

pyAesCrypt, file-encryption script that uses AES256-CBC to decrypt files

-----------------
"""

def encrypt_AesCrypt(file, key):
    """  """
    # encryption/decryption buffer size - 128K
    bufferSize = 128 * 1024
    save_name = file.path + ".aes"
    # encrypt
    with open(str(file.path), "rb") as fIn:
        with open(save_name, "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, key, bufferSize)
    remove(file.path)

def dencrypt_AesCrypt(file, key):
    """  """
    # get encrypted file size
    encFileSize = stat(file.path).st_size
    # encryption/decryption buffer size - 128K
    bufferSize = 128 * 1024
    password = key
    save_name = str(file.name)
    with open(file.path, "rb") as fIn:
        try:
            with open(save_name, "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
            # remove output file on error
            remove(save_name)
