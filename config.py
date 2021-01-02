import os
import configparser


class Config(object):
    def __init__(self):
        jd_user = os.getenv('JD_USER')
        conf_path = './config/config_' + jd_user + '.ini'
        self._path = os.path.join(os.getcwd(), conf_path)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: %s" % conf_path)
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)


global_config = Config()
