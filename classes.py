#Классы будут в этом файле
import blowfish
from os import urandom


class Account:
    """
    __login -> contains users login
    __password -> contains users password
    __cipher -> contains cipher
    __iv -> ??? needed for blowfish
    """

    def encrypt(self):
        if self.__login is not None:
            self.__login = b"".join(self.__cipher.encrypt_cfb(self.__login, self.__iv))
        if self.__password is not None:
            self.__password = b"".join(self.__cipher.encrypt_cfb(self.__password, self.__iv))

    def __init__(self, login="", password=""):
        if login is not None:
            self.__login = login.encode()
        else:
            self.__login = None

        if password is not None:
            self.__password = password.encode()
        else:
            self.__password = None

        self.__cipher = blowfish.Cipher(b'#dskfdfhg#dflg3642/e=wjh+dflwqo22de94hiiwehbsjwk')
        self.__iv = urandom(8)
        self.encrypt()

    def return_account(self):
        if self.__login is not None:
            login_decrypted = b"".join(self.__cipher.decrypt_cfb(self.__login, self.__iv))
        else:
            login_decrypted = b''
        if self.__password is not None:
            pass_decrypted = b"".join(self.__cipher.decrypt_cfb(self.__password, self.__iv))
        else:
            pass_decrypted = b''
        return [login_decrypted.decode(), pass_decrypted.decode()]


class User:
    """
    __accounts -> not really needed dict. Just for now
    __userId -> user id
    __firstName ->
    __lastName ->
    """
    __accounts = {}

    def __init__(self, first_name=None, last_name=None, user_id=None):
        self.__userId = user_id
        self.__firstName = first_name
        self.__lastName = last_name

    def name(self):
        return [self.__firstName, self.__lastName]

    def add_account(self, site, acc):
        if self.__accounts.get(site) is None:
            self.__accounts[site] = acc
            return True
        else:
            return False

    def return_sites(self):
        return self.__accounts.keys()

    def return_account(self, site):
        temp = self.__accounts.get(site)
        if temp is not None:
            return [site, temp.return_account()]
        else:
            return None

    def return_id(self):
        return self.__userId
