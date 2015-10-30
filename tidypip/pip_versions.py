
class PipVersions:
    """ Represents a set of installed packages and their versions """
    
    def __init__(self, versions):
        """ Initialize with the versions """
        self._versions = {}
        self._properNames = {}
        
        for name, version in versions.items():
            lowerName = self._getName(name)
            self._versions[lowerName] = version
            self._properNames[lowerName] = name
            
    def __contains__(self, name):
        """ Return if there is version info for the given name """
        name = self._getName(name)
        return name in self._versions
            
    def __getitem__(self, name):
        """ Return the version info for the given name """
        name = self._getName(name)
        return self._versions[name]
        
    def getProperName(self, name):
        """ Return the Proper Package Name """
        name = self._getName(name)
        return self._properNames[name]
        
    def _getName(self, name):
        """ Return the name ignoring case """
        return name.lower()
        