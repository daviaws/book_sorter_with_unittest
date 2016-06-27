import unittest
import os
from src.mainconfig import MainConfig, InvalidConfigAttr, InvalidConfigFile

CONFIG_PATH = 'config.ini'

class MainConfigTest(unittest.TestCase):

    def test_config_file_exist(self):
        print()
        print('### Configuration tests ###')
        print('Testing config_file exist')
        try:
            cS = MainConfig(CONFIG_PATH)
        except Exception as e:
            if FileNotFoundError == type(e):
                print(e)
                raise
        
    def test_config_file_valid(self):
        print()
        print('Testing config_file valid')
        try:
            cS = MainConfig(CONFIG_PATH)
        except Exception as e:
            if InvalidConfigFile == type(e):
                print(e)
                raise

    def test_config_init_arguments(self):
        print()
        print('Testing config init arguments')
        try:
            cS = MainConfig(CONFIG_PATH)
        except Exception as e:
            if InvalidConfigAttr == type(e):
                print(e)
                raise
        else:
            self.assertIsNotNone(cS.loadINI)
            self.assertIsNotNone(cS.saveINI)
            self.assertIsNotNone(cS.rulesList)

    def test_loadINI_exist(self):
        print()
        print('Testing loadINI exist')
        try:
            cS = MainConfig(CONFIG_PATH)
        except Exception as e:
            pass
        else:
            if not os.path.isfile(cS.loadINI):
                raise FileNotFoundError(cS.loadINI)

    def test_saveINI_creation(self):
        print()
        print('Testing saveINI can be created')
        try:
            cS = MainConfig(CONFIG_PATH)
        except Exception as e:
            pass
        else:
            if not os.path.isfile(cS.saveINI):
                try:
                    test = open(cS.saveINI, 'w')
                except Exception as e:
                    print(e)
                else:
                    test.close()
                    os.remove(cS.saveINI)
