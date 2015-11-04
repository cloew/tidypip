from ..packages import PackageFactory
from kao_command.args import Arg

class PackagesArg(Arg):
    """ Represents an argument that specifies packages """
    
    def __init__(self, *, help):
        """ Initialize the Arg """
        Arg.__init__(self, 'packages', action='store', nargs='+', help=help)
    
    def getValue(self, args):
        """ Return the value from the args """
        packages = Arg.getValue(self, args)
        return PackageFactory.buildAll(packages)