import os
import sys
from pathlib import Path
import configparser

from backports.configparser import ConfigParser

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")

config = configparser.ConfigParser()
config.read(config_path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getValidUserName():
        print("Salman")
        valid_user_name = config.get('common info', 'userName')
        return valid_user_name

    @staticmethod
    def getValidUserPassword():
        valid_password = config.get('common info', 'password')
        return valid_password

    @staticmethod
    def getInValidUserName():
        invalidUser = config.get('common info', 'userName')
        return invalidUser

    @staticmethod
    def getInValidUserPassword():
        invalidpassword = config.get('common info', 'password')
        return invalidpassword


