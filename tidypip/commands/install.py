from kao_command.args import Arg, FlagArg, BareWords
from subprocess import call

class Install:
    """ Command to install a package """
    description = "Install packages"
    args = [Arg('packages', action='store', nargs='+', help='Packages to install')]
        
    def run(self, *, packages):
        """ Run the command """
        call(['pip', 'install'] + packages)