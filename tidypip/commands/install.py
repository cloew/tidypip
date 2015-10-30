from ..pip_wrapper import PipWrapper
from ..packages import NamedPackage
from kao_command.args import Arg, FlagArg

class Install:
    """ Command to install a package """
    description = "Install packages"
    args = [Arg('packages', action='store', nargs='+', help='Packages to install')]
        
    def run(self, *, packages):
        """ Run the command """
        packages = [NamedPackage(package) for package in packages]
        pip = PipWrapper()
        pip.install(packages)