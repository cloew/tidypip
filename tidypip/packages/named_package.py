
class NamedPackage:
    """ Represents a package specified by Name """
    
    def __init__(self, name):
        """ Initialize with the name """
        self.name = name
        
    @property
    def installAs(self):
        """ Return the string to use to Install the package via pip """
        return self.name
        
    def forRequirements(self, versions):
        """ Return the text to use for adding to the Requirements file """
        return "{0}=={1}".format(versions.getProperName(self.name), versions[self.name])