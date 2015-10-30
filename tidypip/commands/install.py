from ..requirements_file import RequirementsFile
from ..pip_wrapper import PipWrapper
from ..packages import NamedPackage

from kao_command.args import Arg, FlagArg

class Install:
    """ Command to install a package """
    description = "Install packages"
    args = [Arg('packages', action='store', nargs='+', help='Packages to install'),
            FlagArg('-s', '--save', action='store_true', help='Save the installed packages to the Requirements File')]
        
    def run(self, *, packages, save):
        """ Run the command """
        packages = [NamedPackage(package) for package in packages]
        pip = PipWrapper()
        pip.install(packages)
        
        if save:
            versions = pip.versions()
            reqFile = RequirementsFile("requirements.txt")
            reqFile.add(packages, versions)