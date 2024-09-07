import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get('data', 'baseURL')
        return url

    @staticmethod
    def getusername():
        user = config.get('data', 'username')
        return user

    @staticmethod
    def get_password():
        passw = config.get('data', 'password')
        return passw

    @staticmethod
    def get_url():
        url2 = config.get('data', 'URL')
        return url2
