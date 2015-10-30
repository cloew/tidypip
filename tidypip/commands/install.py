from ..pip_wrapper import PipWrapper
from kao_command.args import Arg, FlagArg, BareWords

class Install:
    """ Command to install a package """
    description = "Install packages"
    args = [Arg('packages', action='store', nargs='+', help='Packages to install')]
        
    def run(self, *, packages):
        """ Run the command """
        PipWrapper().install(packages)