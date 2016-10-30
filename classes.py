#Классы будут в этом файле

import blowfish
from os import urandom


class Account:

    def __init__(self, login, password):
        self.__login = login.encode()
        self.__password = password.encode()
        self.cipher = blowfish.Cipher(b'#dskfdfhg#dflg3642/e=wjh+dflwqo22de94hiiwehbsjwk')
        self.iv = urandom(8)


    def returnAccount(self):
        return [self.__login, self.__password]


    def encrypt(self):
        login_encrypted = b"".join(self.cipher.encrypt_cfb(self.__login, self.iv))
        pass_encrypted = b"".join(self.cipher.encrypt_cfb(self.__password, self.iv))
        return [login_encrypted, pass_encrypted]


    def decrypt(self, account_encrypted):
        login_decrypted = b"".join(self.cipher.decrypt_cfb(account_encrypted[0], self.iv))
        pass_decrypted = b"".join(self.cipher.decrypt_cfb(account_encrypted[1], self.iv))
        return [login_decrypted.decode(), pass_decrypted.decode()]


class User:
    __accounts = {}

    def __init__(self, first_name, last_name, id):
        self.__userId = id
        self.__first_name = first_name
        self.__last_name = last_name

    def name(self):
        return [self.__first_name, self.__last_name]

    def addAccount(self, site, acc):
        if((self.__accounts).get(site) == None):
            self.__accounts[site] = acc

    def returnAccount(self, site):
        temp = self.__accounts.get(site)
        return [site, temp.returnAccount()]
