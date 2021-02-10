import configparser

config= configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url= config.get('common_info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username= config.get('common_info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password= config.get('common_info', 'password')
        return password