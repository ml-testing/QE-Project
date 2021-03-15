import configparser

config = configparser.RawConfigParser()
config.read("../configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getappurl():
        url = config.get("inputs", "siteURL")
        return url

    @staticmethod
    def getemail():
        email = config.get("inputs", "email")
        return email

    @staticmethod
    def getpassword():
        password = config.get("inputs", "password")
        return password

    @staticmethod
    def getfirstname():
        firstname = config.get("inputs", "firstname")
        return firstname

    @staticmethod
    def getlasttname():
        lastname = config.get("inputs", "lastname")
        return lastname
