import os
import encrypter

class File:
    def __init__(self, name, path, encryption_method):
        self.name = name
        self.path = path
        self.encryption_method = encryption_method

        self.directory = {
            "name" : self.name,
            "path" : self.path,
            "encryption_method" : self.encryption_method
        }

    def encrypte(self, key):
        encrypter.encrypt_AesCrypt(self, key)

    def decrypte(self, key):
        encrypter.dencrypt_AesCrypt(self, key)

    def remove(self):
        os.remove(self.path)

    def save_obj(self):
        pass


def new_dir(dir_name):
    path = "files/" + str(dir_name)
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass

def files_in_dir():
    path = "files/"
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
