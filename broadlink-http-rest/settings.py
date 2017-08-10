import configparser
from os import path

applicationDir = path.dirname(path.abspath(__file__))
settingsINI = path.join(applicationDir, 'settings.ini')

settings = configparser.ConfigParser()
settings.read(settingsINI)

Timeout = settings.get('General', 'Timeout')

RMIPAddress = settings.get('BroadlinkRM', 'IPAddress')
RMPort = settings.get('BroadlinkRM', 'Port')
RMMACAddress = settings.get('BroadlinkRM', 'MACAddress')
