from .commands import commands
from kao_command import Driver

def TidyPip(scriptName):
    return Driver(scriptName, commands)