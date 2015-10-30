
class NamedPackage:
    """ Represents a package specified by Name """
    
    def __init__(self, name):
        """ Initialize with the name """
        self.name = name
        
    @property
    def installAs(self):
        """ Return the string to use to Install the package via pip """
        return self.name