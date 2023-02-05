import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_app_url():
        url = config.get('basic data', 'baseurl')
        return url
