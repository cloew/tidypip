from ..requirements_file import RequirementsFile
from ..pip_wrapper import PipWrapper
from ..args import PackagesArg

from kao_command.args import FlagArg

class Install:
    """ Command to install a package """
    description = "Install packages"
    args = [PackagesArg(help='Packages to install'),
            FlagArg('-s', '--save', action='store_true', help='Save the installed packages to the Requirements File'),
            FlagArg('-p', '--pip', action='store', help='The Pip command to use')]
        
    def run(self, *, packages, save, pip):
        """ Run the command """
        pip = PipWrapper(pipCmd=pip)
        pip.install(packages)
        
        if save:
            versions = pip.versions()
            reqFile = RequirementsFile("requirements.txt")
            reqFile.add(packages, versions)