
class RequirementsFile:
    """ Represents a PIP Requirements File """
    
    def __init__(self, path):
        """ Initialize with the path """
        self.path = path
        
    def add(self, packages, versions):
        """ Add the given packages to the file """
        with open(self.path, 'a') as file:
            for package in packages:
                file.write(package.forRequirements(versions)+'\n')