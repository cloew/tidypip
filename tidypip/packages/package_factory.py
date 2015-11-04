from .named_package import NamedPackage
from .url_package import UrlPackage

class PackageFactory:
    """ Factory to construct Packages """
    
    def buildAll(self, packages):
        """ Build all the given packages """
        return [self.build(package) for package in packages]
    
    def build(self, package):
        """ Build the package """
        if '/' in package:
            return UrlPackage(package)
        else:
            return NamedPackage(package)
            
PackageFactory = PackageFactory()